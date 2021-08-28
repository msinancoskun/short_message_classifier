from tkinter import *
from tkinter import ttk
# import docclass


class SMSClassifier:

    def __init__(self, main):
        self.main = main
        main.title("SMS Classifier")
        main.columnconfigure(0, weight=2)

        # Header Text
        self.header = Label(main, text='Short Message Classifier', bg="sky blue", fg="white", font=('', 30))
        self.header.grid(row=0, columnspan=2)

        # Load Dataset Button
        self.load_button = Button(text='Load Dataset', command=self.load_dataset)
        self.load_button.grid(row=1, sticky='w', padx=(100, 0), pady=(20, 0))

        # Dataset Loaded Textbox info
        self.load_textbox = Text(main, wrap=NONE, height=3, width=60)
        self.load_textbox.grid(row=1, column=1, padx=(0, 150), pady=(20, 0))

        # Classifier and threshold labels
        self.classifier_label = Label(main, text="Choose Classifier", fg="yellow", bg="sky blue", font=('', 15))
        self.classifier_label.grid(row=2, column=0, sticky='e', padx=(50, 0), pady=(50, 0))

        self.set_threshold = Label(main, text="Set Thresholds", fg="yellow", bg="sky blue", font=('', 15))
        self.set_threshold.grid(row=2, column=1, sticky='w', padx=(100, 0), pady=(50, 0))

        # Radio Buttons
        self.classify_methods = StringVar()
        self.naive_bayes = Radiobutton(main, text='Naive-Bayes', variable=self.classify_methods, val='Naive-Bayes',
                                       bg='sky blue', font=('', 13))
        self.naive_bayes.grid(row=3, column=0, sticky='w', padx=(70, 0), pady=10)

        self.fisher = Radiobutton(main, text='Fisher', variable=self.classify_methods, val='Fisher', bg='sky blue',
                                  font=('', 13))
        self.fisher.grid(row=4, column=0, sticky='w', padx=(70, 0))

        # Combo Box
        self.combo_box = ttk.Combobox(main, state='readonly')
        self.combo_box['values'] = ['SPAM', 'HAM']
        self.combo_box.grid(row=3, column=1, sticky='w', padx=(100, 0))

        # Listbox
        self.listbox = Listbox(main, height=2, selectmode=SINGLE)
        self.listbox.grid(row=3, column=1, sticky='e', padx=(0, 175))

        # Set Button
        self.set_button = Button(text="Set", command=self.set_threshold_)
        self.set_button.grid(row=3, column=1, padx=(0, 50), pady=(20, 0))

        # Thresholds
        self.threshold_variable = StringVar()
        self.threshold_entry = Entry(main, textvariable=self.threshold_variable, width=4)
        self.threshold_entry.grid(row=3, column=1, sticky='w', padx=(50, 0))

        # Remove Button
        self.remove_button = Button(main, text="Remove\nSelected", command=self.remove_threshold)
        self.remove_button.grid(row=3, column=1, sticky='e', padx=(0, 80), pady=(20, 0))

        # Calcualte Button
        self.calculate_button = Button(main, text="Calculate Accuracy", command=self.calculate_accuracy)
        self.calculate_button.grid(row=5, column=0, sticky='e', padx=(0, 80), pady=(30, 10))

        # Accuracy textbox
        self.accuracy_textbox = Text(main, height=10, width=120)
        self.accuracy_textbox.grid(row=6, column=0, columnspan=2, padx=5, pady=(0, 20))

    def load_dataset(self):
        """ This method loads the dataset from the given text file. """
        self.load_textbox.delete('1.0', END)
        self.load_textbox.update_idletasks()
        self.sms_lines = []

        with open('SMSSpamCollection.txt') as sms_data:
            for line in sms_data:
                self.sms_lines.append(line)
        print(len(self.sms_lines))
        if len(self.sms_lines) > 0:
            self.load_textbox.insert(END, 'Dataset Loaded')
        else:
            self.load_textbox.insert(END, 'Loading dataset has failed...')

    def set_threshold_(self):
        if self.combo_box.get() == 'HAM':
            for item in self.listbox.get(0, END):
                if 'HAM' in item:
                    self.listbox.delete(item)
            if self.threshold_variable.get():
                ham_string = 'HAM- ' + self.threshold_variable.get()
                self.listbox.insert(END, ham_string)

        if self.combo_box.get() == 'SPAM':
            for item in self.listbox.get(0, END):
                if 'SPAM' in item:
                    self.listbox.delete(item)
            if self.threshold_variable.get():
                spam_string = 'SPAM- ' + self.threshold_variable.get()
                self.listbox.insert(END, spam_string)

    def remove_threshold(self):
        """ Removes the selected item from the listbox. """
        self.listbox.delete(self.listbox.curselection())

    def calculate_accuracy(self):
        self.accuracy_textbox.delete('1.0', END)
        self.accuracy_textbox.update_idletasks()

        average_spam = 0
        average_ham = 0

        print(average_ham, average_spam)


if __name__ == '__main__':
    mainWindow = Tk()
    app = SMSClassifier(mainWindow)
    mainWindow.mainloop()
