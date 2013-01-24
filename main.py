from flask import Flask
from flask import render_template
app = Flask(__name__)

# import events list
from models import events


@app.route('/')
def index():
    return render_template(
        'index.html',
        pastevents=events.pastevents,
        upcomingevents=events.upcomingevents
    )

@app.route('/faq')
def faq():
    return render_template(
        'faq.html'
    )


@app.route('/about')
def aboutus():
    return render_template(
        'about.html'
    )



@app.route('/schedule')
def schedule():
    return render_template(
        'schedule.html',
        pastevents=events.pastevents,
        upcomingevents=events.upcomingevents
    )


@app.route('/materials')
def materials():
    return render_template(
        'materials.html'
    )


@app.route('/materials/html5')
def materials_html_workshop():
    return render_template(
        'materials/html5workshop.html'
    )


@app.route('/materials/gitjquery')
def materials_gitjquery():
    return render_template(
        'materials/gitjquery.html'
    )


if __name__ == "__main__":
    app.run()
