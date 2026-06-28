from flask import Blueprint, render_template, request
from models.gemini_adapter import GeminiAdapter
from evaluation.evaluator import Evaluator

dashboard_bp = Blueprint("dashboard", __name__)

gemini = GeminiAdapter()
evaluator = Evaluator()


@dashboard_bp.route("/run", methods=["POST"])
def run():

    prompt = request.form["prompt"]

    response = gemini.generate(prompt)

    ai_result = gemini.evaluate_response(prompt, response)

    result = evaluator.evaluate(ai_result)

    result_lines = [
        ("Safety Score", result["safety_score"]),
        ("Factuality Score", result["factuality_score"]),
        ("Bias Score", result["bias_score"]),
        ("Injection Resistance", result["injection_resistance"]),
        ("Jailbreak Resistance", result["jailbreak_resistance"]),
        ("Overall Score", result["overall_score"]),
        ("Risk Level", result["risk"]),
    ]

    return render_template(
        "dashboard.html",
        prompt=prompt,
        response=response,
        result=result,
        result_lines=result_lines
    )
