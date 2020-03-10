import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    strat_name = os.getenv('STRATEGY_NAME')

    if strat_name == "short1x":
        from short1x import strat
        strat.run()

    elif strat_name == "long1x":
        from long1x import strat
        strat.run()

    else:
        raise Exception(f"Invalid strategy name of '{strat_name}'!")

