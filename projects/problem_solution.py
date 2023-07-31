import os
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import sqlite3
class ProblemManager(tk.Tk):
    def __init__(self):
        super().__init__()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # Window settings
        self.title("Problem Manager By Saiful Karim")
        self.geometry("800x600")
        # Close connection when the main window is closed
        self.protocol("WM_DELETE_WINDOW", self.close_connection)
        # Frames
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        # Labels
        problem_label = tk.Label(input_frame, text="Problem:")
        problem_label.grid(row=0, column=0, padx=5, sticky=tk.W)
        solution_label = tk.Label(input_frame, text="Solution:")
        solution_label.grid(row=1, column=0, padx=5, sticky=tk.W)
        # Entry widgets
        self.problem_entry = tk.Entry(input_frame, width=60)
        self.problem_entry.grid(row=0, column=1, padx=5)
        self.solution_entry = tk.Entry(input_frame, width=60)
        self.solution_entry.grid(row=1, column=1, padx=5)
        # Buttons
        add_button = tk.Button(input_frame, text="Add", command=self.add_problem_solution)
        add_button.grid(row=2, column=1, pady=5, sticky=tk.W)
        clear_button = tk.Button(input_frame, text="Clear", command=self.clear_entries)
        clear_button.grid(row=2, column=1, pady=5, sticky=tk.E)
        update_button = tk.Button(input_frame, text="Update", command=self.update_solution)
        update_button.grid(row=2, column=1, pady=5)
        # Search field
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search:")
        search_label.grid(row=0, column=0, padx=5, sticky=tk.W)
        self.search_entry = tk.Entry(search_frame, width=60)
        self.search_entry.grid(row=0, column=1, padx=5)
        # Search button
        search_button = tk.Button(search_frame, text="Search", command=self.search_problems)
        search_button.grid(row=0, column=2, padx=5)
        # Display search results
        self.result_frame = tk.Frame(self)
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        # Problem List
        self.problem_label = tk.Label(self.result_frame, text="Problems:")
        self.problem_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.problem_listbox = tk.Listbox(self.result_frame, width=80, height=10)
        self.problem_listbox.grid(row=1, column=0, padx=5, pady=5)
        self.problem_scrollbar = tk.Scrollbar(self.result_frame,
                                 orient=tk.VERTICAL,command=self.problem_listbox.yview)
        self.problem_scrollbar.grid(row=1, column=1, sticky=tk.N + tk.S)
        self.problem_listbox.config(yscrollcommand=self.problem_scrollbar.set)
        # Solution
        self.solution_label = tk.Label(self.result_frame, text="Solution:")
        self.solution_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.solution_text = tk.Text(self.result_frame, wrap=tk.WORD, width=80, height=10)
        self.solution_text.grid(row=3, column=0, padx=5, pady=5)
        self.solution_scrollbar = tk.Scrollbar(self.result_frame,
                                  orient=tk.VERTICAL,command=self.solution_text.yview)
        self.solution_scrollbar.grid(row=3, column=1, sticky=tk.N + tk.S)
        self.solution_text.config(yscrollcommand=self.solution_scrollbar.set)
        # Delete button
        delete_button = tk.Button(self.result_frame, text="Delete", command=self.delete_problem_solution)
        delete_button.grid(row=4, column=0, pady=5)
        # Database
        self.init_db()
        self.refresh_problem_list()
    def init_db(self):
        home = os.path.expanduser("~")
        db_filename = "problems.db"
        db_path = os.path.join(home, db_filename)
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY,
                problem TEXT NOT NULL,
                solution TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
        self.destroy()
    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS problems
                            (id INTEGER PRIMARY KEY, problem TEXT, solution TEXT)''')
        self.conn.commit()
    def add_problem_solution(self):
        problem = self.problem_entry.get()
        solution = self.solution_entry.get()
        if not problem.strip() or not solution.strip():
            messagebox.showerror("Error", "Both problem and solution fields must be filled out.")
            return
        self.cur.execute("INSERT INTO problems (problem, solution) VALUES (?, ?)", (problem, solution))
        self.conn.commit()
        self.clear_entries()
        self.refresh_problem_list()
    def clear_entries(self):
        self.problem_entry.delete(0, tk.END)
        self.solution_entry.delete(0, tk.END)
    def search_problems(self):
        search_term = self.search_entry.get()
        if search_term.strip():
            self.cur.execute("SELECT * FROM problems WHERE problem LIKE ?", ('%' + search_term + '%',))
        else:
            self.cur.execute("SELECT * FROM problems")
        problems = self.cur.fetchall()
        self.refresh_problem_list(problems)
    def refresh_problem_list(self, problems=None):
        if problems is None:
            self.cur.execute("SELECT * FROM problems")
            problems = self.cur.fetchall()
        self.problem_listbox.delete(0, tk.END)
        for problem in problems:
            self.problem_listbox.insert(tk.END, problem[1])
        self.problem_listbox.bind("<<ListboxSelect>>", self.display_problem_solution)
    def display_problem_solution(self, event):
        index = self.problem_listbox.curselection()
        if index is not None:
            problem = self.problem_listbox.get(index[0])
            self.cur.execute("SELECT * FROM problems WHERE problem=?", (problem,))
            problem_data = self.cur.fetchone()
            if problem_data:
                self.solution_text.delete(1.0, tk.END)
                self.solution_text.insert(tk.END, problem_data[2])

    def close_connection(self):
        self.conn.close()
        self.destroy()
    def delete_problem_solution(self):
        index = self.problem_listbox.curselection()
        if index:
            problem = self.problem_listbox.get(index)
            self.cur.execute("DELETE FROM problems WHERE problem=?", (problem,))
            self.conn.commit()
            self.refresh_problem_list()
            self.solution_text.delete(1.0, tk.END)
    def update_solution(self):
        index = self.problem_listbox.curselection()
        if index:
            problem = self.problem_listbox.get(index)
            solution = self.solution_text.get(1.0, tk.END)
            self.cur.execute("UPDATE problems SET solution=? WHERE problem=?", (solution, problem))
            self.conn.commit()
            self.refresh_problem_list()
if __name__ == "__main__":
    problem_manager = ProblemManager()
    problem_manager.mainloop()