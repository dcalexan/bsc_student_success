{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "816e862d-eba1-4a81-88d6-08636fdcb59a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting Flask\n",
      "  Downloading Flask-2.0.1-py3-none-any.whl (94 kB)\n",
      "Collecting itsdangerous>=2.0\n",
      "  Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)\n",
      "Requirement already satisfied: Jinja2>=3.0 in c:\\users\\pvanzand\\anaconda3\\envs\\mlearn\\lib\\site-packages (from Flask) (3.0.1)\n",
      "Collecting click>=7.1.2\n",
      "  Downloading click-8.0.1-py3-none-any.whl (97 kB)\n",
      "Collecting Werkzeug>=2.0\n",
      "  Downloading Werkzeug-2.0.1-py3-none-any.whl (288 kB)\n",
      "Requirement already satisfied: colorama in c:\\users\\pvanzand\\anaconda3\\envs\\mlearn\\lib\\site-packages (from click>=7.1.2->Flask) (0.4.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\pvanzand\\anaconda3\\envs\\mlearn\\lib\\site-packages (from Jinja2>=3.0->Flask) (2.0.1)\n",
      "Installing collected packages: Werkzeug, itsdangerous, click, Flask\n",
      "Successfully installed Flask-2.0.1 Werkzeug-2.0.1 click-8.0.1 itsdangerous-2.0.1\n"
     ]
    }
   ],
   "source": [
    "#!pip install Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8636520-afb8-4b11-be7d-9d04899b2f0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, send_from_directory, render_template, request, redirect, url_for"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cd69a4de-e17e-426e-8fbe-8d20c3bcaeaf",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# save this as app.py\n",
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def hello():\n",
    "    return \"Hello, World!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d1dc441-09e9-4a1e-af9c-5e74065e3bfd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db487f79-5a69-4095-a6ca-27f297d4f0c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8579c4f-2cef-484d-b63d-3830738c0f6b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "169e8fad-ead7-4090-b18c-f88c0533565b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
