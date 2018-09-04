import json
import sys
import os

import rasa_core
from rasa_core import run
from gevent.pywsgi import WSGIServer
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter, NaturalLanguageInterpreter
from rasa_core.policies import FallbackPolicy, MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_nlu.config import load
from rasa_nlu.model import Interpreter
from rasa_nlu.model import Trainer
from rasa_nlu.training_data import load_data


def warn(*args, **kwargs):
    pass


import warnings

warnings.warn = warn

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def train_nlu():
    training_data = load_data('data/nlu.md')
    conf = load("nlu_config.yml")
    trainer = Trainer(conf)
    trainer.train(training_data)
    model_directory = trainer.persist("models", project_name="nlu", fixed_model_name="current")
    print("persisted model to ", model_directory)
    file = open("models/nlu/latest.txt", 'w')
    file.write(model_directory)
    file.close()


def do_nlu_eval(txt):
    file = open("models/nlu/latest.txt", 'r')
    model_dir = file.readline()
    interpreter = Interpreter.load(model_dir=model_dir)
    return interpreter.parse(txt)


def get_interpreter():
    """ in python console verwenden:
    from dev_targets import get_interpreter()
    nterp = get_interpreter()
    nterp.parse('kennst du Chuck Norris?')
    """
    file = open("models/nlu/latest.txt", 'r')
    model_dir = file.readline()
    interpreter = Interpreter.load(model_dir=model_dir)
    return interpreter


def train_dialog(online=False, nlu=True):
    ## TODO bei sehr wenig stories - wie am Anfang - probiert erst memoization unk keras
    # agent = Agent("domain.yml", policies=[MemoizationPolicy(), KerasPolicy()])
    ## TODO sobald der Bot ein wenig stabil wird, nach ein duzent Stories oder so, probiere nur Keras
    ##agent = Agent("domain.yml", policies=[KerasPolicy(),fallback])
    agent = Agent("domain.yml", policies=[KerasPolicy()])
    stories_file = "data\stories"
    stories_data = agent.load_data(stories_file)
    output_path = "models\dialog"
    kwargs = {"epochs": 100}
    agent.train(
        stories_data,
        validation_split=0.2,
        **kwargs
    )
    agent.persist(output_path)


def init_debug_logging():
    import logging
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

def redirect_stderr():
    import os
    import sys
    f = open(os.devnull, 'w')
    sys.stderr = f

def runbot(dbug=False, online_training=False):
    redirect_stderr()
    if dbug:
        init_debug_logging()
    interpreter = NaturalLanguageInterpreter.create("models/nlu/current")
    from rasa_core.utils import EndpointConfig
    action_endpoint = EndpointConfig(url="http://localhost:5056/webhook")
    agent = Agent.load("models/dialog", interpreter=interpreter, action_endpoint=action_endpoint)
    if online_training:
        from rasa_core.train import online
        online.serve_agent(agent)
    else:
        rasa_core.run.serve_application(agent, channel='cmdline')


def start_action_server():
    from rasa_core_sdk.endpoint import endpoint_app
    import logging
    init_debug_logging()
    logger = logging.getLogger()
    edp_app = endpoint_app(action_package_name="backend")
    http_server = WSGIServer(('0.0.0.0', 5056), edp_app)
    http_server.start()
    logger.info("Action endpoint is up and running. on {}"
                "".format(http_server.address))
    http_server.serve_forever()


if __name__ == '__main__':
    ## Main Methode
    ## Aufrufen von Projekt Dir aus mit --> python dev_targets
    ## python dev_targets help für Hilfe
    src_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    os.chdir(src_dir)
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command in ("h", "help"):
            print("USAGE:")
            print("python dev_targets <target> <option>")
            print("TARGETS: ")
            print("actions -- start action server: ")
            print("train_nlu -- train (und persistieren) das NLU Modell mit Daten in nlu.md.")
            print("train_dialog -- train (und persistieren) das dialog Modell mit Daten in stories folder")
            print("train_interactive -- interaktives Dialog-Trainieren starten")
            print("run -- startet den Bot in der Konsole.")
            print("run d -- startet den Bot in der Konsole mit debug-Ausgaben")
            print("eval_nlu '<evalstring>' evaluiert ein Eingabe-String und liefert Ergebnisse von NLU Modell zurück")
            print("setup_db -- Datenbank initialisieren (muss Aufgabe-spezifisch implementiert werden")
            print("eval_sql <'sql'> <(params)> sql gegen db feuern und ergebnisse bekommen")

        elif command == "eval_nlu":
            if len(sys.argv) < 3:
                print("please provide a string to evaluate")
            else:
                txt = sys.argv[2]
                eval_result = do_nlu_eval(txt)
                print(json.dumps(eval_result, indent=4))
        elif command == "train_nlu":
            train_nlu()
        elif command == "train_dialog":
            train_dialog()
        elif command == "train_interactive":
            runbot(online_training=True)
        elif command == "run":
            dbug = False
            if len(sys.argv) >= 3:
                arg = sys.argv[2]
                if arg == 'd':
                    dbug = True
            runbot(dbug)
        elif command == "setup_db":
            from bundesbot.backend.backend import Backend
            back = Backend()
            back.setup()
        elif command == "eval_sql":
            if len(sys.argv) >= 3:
                query = sys.argv[2]
                from bundesbot.backend.backend import Backend

                back = Backend()
                back.eval(query)
        elif command == "actions":
            start_action_server()
