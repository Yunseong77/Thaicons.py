import tkinter as tk
import random

# Thai consonants with their names
thai_consonants = [
    ("ก", "กอ ไก่"), ("ข", "ขอ ไข่"), ("ฃ", "ฃอ ขวด"), ("ค", "คอ ควาย"),
    ("ฅ", "ฅอ คน"), ("ฆ", "ฆอ ระฆัง"), ("ง", "งอ งู"), ("จ", "จอ จาน"),
    ("ฉ", "ฉอ ฉิ่ง"), ("ช", "ชอ ช้าง"), ("ซ", "ซอ โซ่"), ("ฌ", "ฌอ เฌอ"),
    ("ญ", "ญอ หญิง"), ("ฎ", "ฎอ ชฎา"), ("ฏ", "ฏอ ปฏัก"), ("ฐ", "ฐอ ฐาน"),
    ("ฑ", "ฑอ มณโฑ"), ("ฒ", "ฒอ ผู้เฒ่า"), ("ณ", "ณอ เณร"), ("ด", "ดอ เด็ก"),
    ("ต", "ตอ เต่า"), ("ถ", "ถอ ถุง"), ("ท", "ทอ ทหาร"), ("ธ", "ธอ ธง"),
    ("น", "นอ หนู"), ("บ", "บอ ใบไม้"), ("ป", "ปอ ปลา"), ("ผ", "ผอ ผึ้ง"),
    ("ฝ", "ฝอ ฝา"), ("พ", "พอ พาน"), ("ฟ", "ฟอ ฟัน"), ("ภ", "ภอ สำเภา"),
    ("ม", "มอ ม้า"), ("ย", "ยอ ยักษ์"), ("ร", "รอ เรือ"), ("ล", "ลอ ลิง"),
    ("ว", "วอ แหวน"), ("ศ", "ศอ ศาลา"), ("ษ", "ษอ ฤๅษี"), ("ส", "สอ เสือ"),
    ("ห", "หอ หีบ"), ("ฬ", "ฬอ จุฬา"), ("อ", "ออ อ่าง"), ("ฮ", "ฮอ นกฮูก")
]

class ThaiFlashGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flash Game")
        self.root.geometry("400x300")
        
        self.current_card = None
        self.flipped = False
        
        self.canvas = tk.Canvas(root, width=300, height=200, bg="white", highlightthickness=2)
        self.canvas.pack(pady=20)
        
        self.text_id = self.canvas.create_text(150, 100, text="", font=("Arial", 40, "bold"))
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack()
        
        self.next_card()
    
    def next_card(self):
        self.flipped = False
        self.current_card = random.choice(thai_consonants)
        self.canvas.itemconfig(self.text_id, text=self.current_card[0])
    
    def flip_card(self):
        if self.current_card:
            if self.flipped:
                self.canvas.itemconfig(self.text_id, text=self.current_card[0])
            else:
                self.canvas.itemconfig(self.text_id, text=self.current_card[1])
            self.flipped = not self.flipped

if __name__ == "__main__":
    root = tk.Tk()
    game = ThaiFlashGame(root)
    root.mainloop()