import customtkinter
import requests
import json
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
	width = 900
	height = 600

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.title("Data Leak Prevetion System Client")
		self.geometry(f"{self.width}x{self.height}")
		self.resizable(False, False)
		self.draw_login()

	def draw_login(self):
		# create login frame
		self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
		self.login_frame.grid(row=0, column=0, sticky="ns")
		self.login_label = customtkinter.CTkLabel(self.login_frame, text="DLP\nАвторизация", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
		self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Идентификатор")
		self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
		self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Ключ")
		self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
		self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
		self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

	def draw_main(self):
		# create main frame
		self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
		self.main_frame.grid(row=1, column=1)
		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_label = customtkinter.CTkLabel(self.main_frame, text="DLP\nГлавная", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.main_label.grid(row=0, column=0, padx=30, pady=(150, 15))
		self.scan_button = customtkinter.CTkButton(self.main_frame, text="Начать сканирование", command=self.back_event, width=200)
		self.scan_button.grid(row=1, column=0, padx=30, pady=(15, 15))
		self.back_button = customtkinter.CTkButton(self.main_frame, text="Выход", command=self.back_event, width=200)
		self.back_button.grid(row=2, column=0, padx=30, pady=(15, 15))

	def draw_error_login(self):
		# create main frame
		self.error_login_frame = customtkinter.CTkFrame(self, corner_radius=0)
		self.error_login_frame.grid(row=1, column=1)
		self.error_login_frame.grid_columnconfigure(0, weight=1)
		self.error_login_label = customtkinter.CTkLabel(self.error_login_frame, text="DLP\nНеверный идентификатор или ключ.", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.error_login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
		self.back_button = customtkinter.CTkButton(self.error_login_frame, text="Back", command=self.back_error_event, width=200)
		self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

	def login_event(self):
		print("Login pressed - uuid:", self.username_entry.get(), "key:", self.password_entry.get())
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		response = requests.post('http://127.0.0.1:8000/api/v1/auth/check/', json={'uuid': self.username_entry.get(), 'key': self.password_entry.get()}, headers=headers)
		self.login_frame.grid_forget()  # remove login frame
		if response.status_code == 201:
			self.draw_main()
			self.main_frame.grid(row=0, column=0, sticky="nsew")  # show main frame
		else:
			self.draw_error_login()
			self.error_login_frame.grid(row=0, column=0, sticky="nsew")  # show main frame

	def back_event(self):
		self.main_frame.grid_forget()  # remove main frame

		self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

	def back_error_event(self):
		self.error_login_frame.grid_forget()  # remove main frame

		self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
	app = App()
	app.mainloop()
