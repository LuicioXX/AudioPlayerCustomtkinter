from audioplayer import AudioPlayer
import customtkinter
import CTkMessagebox

class AudioPlayerApp:

    def __init__(self):
        # Set window properties
        self.main_window = customtkinter.CTk()
        self.main_window.geometry("500x500")
        self.main_window.title("AudioPlayer made with ♥")

        #AudioInstance
        self.audio_player: AudioPlayer

        # Label 1
        self.label_1 = customtkinter.CTkLabel(self.main_window, text="Put a file path in the input field and press the play button or the stop button...")
        self.label_1.pack(pady=20)

        #Input field
        self.input_path = customtkinter.CTkEntry(self.main_window, placeholder_text="Your file path -->")
        self.input_path.pack(pady=10)

        # Buttons Run and Stop
        self.run_button = customtkinter.CTkButton(self.main_window, text="Play", command=self.play)
        self.run_button.pack(pady=10)

        self.stop_button = customtkinter.CTkButton(self.main_window, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        # Run window in loop event
        self.main_window.mainloop()


    def play(self):
        try:
            self.audio_player = AudioPlayer(self.input_path.get())
            self.audio_player.play(loop=True)

        except:
            print("ERROR")
            CTkMessagebox.CTkMessagebox(self.main_window, message="ERROR: Please be sure your file path is correct! Example: C:/Users/username/Documents", icon="cancel")
    def stop(self):
        self.audio_player.stop()


AudioPlayerApp()





