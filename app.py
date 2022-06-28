import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        reply = request.form["reply"]
        response = openai.Completion.create(
            model="text-davinci-002",
            # model="text-curie-001",
            prompt=generate_prompt(reply),
            temperature=0.7,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(reply):
    return """Make reply to be more verbose, polite, happy and cheerful.

Reply: No
Output: No, but I really appreciate you asking.

Reply: Perhaps
Output: That's an interesting question. I'm unsure. Let me think on it. Thanks for seeking my input.

Reply: Yes
Output: Yes, definitely! That sounds great. Thank you for asking.

Reply: Who cares!
Output: Thanks for asking, but I'm not sure that's really for me.

Reply: Whatever
Output: Whatever you think might be best. I value your opinion.

Reply: Bye
Output: Goodbye, speak soon!

Reply: {}
Output:""".format(
            reply.capitalize()
    )
