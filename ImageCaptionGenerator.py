import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
# Заглушка для функции анализа изображения
def generate_image_description(image_path):
    # Здесь должен быть ваш код или вызов API для анализа изображения и генерации описания
    return "Описание изображения будет здесь."

class ImageDescriptionGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор описания изображения")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        self.choose_image_btn = tk.Button(self.frame, text="Выбрать изображение", command=self.load_image)
        self.choose_image_btn.pack()
        
        self.image_label = tk.Label(self.frame)
        self.image_label.pack(pady=10)
        
        self.description_label = tk.Label(self.frame, text="Описание изображения появится здесь.", wraplength=400)
        self.description_label.pack(pady=10)
    
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            
            description = generate_image_description(file_path)
            self.description_label.config(text=description)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDescriptionGeneratorApp(root)
    root.mainloop()

