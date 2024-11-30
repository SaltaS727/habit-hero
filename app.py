from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Sample task categories and tasks
tasks_by_category = {
    "Morning Habits": ["Brush your teeth", "Make your bed", "Exercise for 10 minutes", "Eat breakfast", "Drink water"],
    "Chores": ["Clean your room", "Help with dishes", "Water the plants"],
    "Learning and Growth": ["Read for 15 minutes", "Practice math", "Practice handwriting"]
}

@app.route('/')
def index():
    total_score = session.get('total_score', 0)
    # Pass tasks_by_category to the index.html template
    return render_template('index.html', total_score=total_score, tasks_by_category=tasks_by_category)

@app.route('/tasks/<category>')
def tasks(category):
    tasks = tasks_by_category.get(category, [])
    return render_template('tasks_by_category.html', category_name=category, tasks=tasks)

@app.route('/tasks/<category>', methods=['POST'])
def submit_tasks(category):
    completed_tasks = request.form.getlist('completed_tasks')
    score = len(completed_tasks) * 10  # 10 points per completed task
    session['total_score'] = session.get('total_score', 0) + score
    return redirect(url_for('index'))

@app.route('/reset_score')
def reset_score():
    session['total_score'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
