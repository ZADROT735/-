from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Хранилище профилей авторов (в реальном приложении используйте базу данных)
profiles = []

@app.route('/')
def index():
    return render_template('index.html', profiles=profiles)

@app.route('/create_profile', methods=['POST'])
def create_profile():
    name = request.form['name']
    bio = request.form['bio']
    vocabulary = request.form['vocabulary']
    theme = request.form['theme']
    tone = request.form['tone']
    
    profile = {
        'name': name,
        'bio': bio,
        'vocabulary': vocabulary,
        'theme': theme,
        'tone': tone,
    }
    profiles.append(profile)
    return redirect(url_for('index'))

@app.route('/generate_article', methods=['POST'])
def generate_article():
    theme = request.form['theme']
    length = int(request.form['length'])
    profile_name = request.form['profile']
    
    # Генерация текста (здесь должен быть вызов к языковой модели)
    generated_text = f"Статья на тему '{theme}' с длиной {length} токенов.\n\n" + " ".join(random.choices(["Lorem ipsum dolor sit amet.", "Consectetur adipiscing elit.", "Sed do eiusmod tempor incididunt."], k=length))
    
    return render_template('article.html', text=generated_text, profile=profile_name)

if __name__ == '__main__':
    app.run(debug=True)