from pathlib import Path
import sys
import connexion # type: ignore
root_path = Path(__file__).parent.parent
sys.path.append(str(root_path))


app =  connexion.FlaskApp(__name__)

app.add_api(root_path / "RestAPI" / "load_balancer_proxy_api.yaml") # type: ignore

if __name__ == "__main__":
    app.run() # type: ignore 