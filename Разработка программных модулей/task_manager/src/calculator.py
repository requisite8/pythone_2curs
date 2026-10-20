import operator
import tkinter as tk

OPERATIONS = ["*", "%", "+", "-", "="]
FUNCTIONS = {"*": operator.mul, "%": operator.mod, "+": operator.add, "-": operator.sub}
MAX_DIGITS = 12

state = {"left": "", "op": "", "right": "", "done": False, "label": None}


def show():
    state["label"].config(text=state["left"] + state["op"] + state["right"] or "0")


def reset():
    state.update(left="", op="", right="", done=False)


def calculate():
    try:
        return str(FUNCTIONS[state["op"]](int(state["left"]), int(state["right"])))
    except ZeroDivisionError:
        reset()
        state["label"].config(text="Ошибка")
        return None


def add_digit(digit):
    if state["done"]:
        reset()
    key = "right" if state["op"] else "left"
    if len(state[key]) < MAX_DIGITS:
        state[key] = str(int(state[key] + digit))
    show()


def set_operation(sign):
    if not state["left"]:
        return
    if state["right"]:
        result = calculate()
        if result is None:
            return
        state.update(left=result, right="")
    state.update(op=sign, done=False)
    show()


def finish():
    if not (state["left"] and state["op"] and state["right"]):
        return
    result = calculate()
    if result is None:
        return
    state.update(left=result, op="", right="", done=True)
    show()


def add_operator(sign):
    if sign == "=":
        finish()
    else:
        set_operation(sign)


def press(value):
    if value.isdigit():
        add_digit(value)
    else:
        add_operator(value)


def create_window():
    root = tk.Tk()
    root.title("Калькулятор")
    root.resizable(False, False)

    text_input = tk.Label(root, text="0", anchor="e", font=("Arial", 24), bg="white", relief="sunken")
    text_input.grid(row=0, column=0, columnspan=4, sticky="we", padx=4, pady=4)
    state["label"] = text_input

    for index, digit in enumerate("7894561230"):
        tk.Button(root, text=digit, width=5, height=2, command=lambda value=digit: press(value)).grid(row=index // 3 + 1, column=index % 3)

    for index, sign in enumerate(OPERATIONS):
        button = tk.Button(root, text=sign, width=5, height=2, command=lambda value=sign: press(value))
        button.grid(row=index + 1, column=3)
    button.grid(row=5, column=0, columnspan=4, sticky="we")
    return root


def main():
    create_window().mainloop()


if __name__ == "__main__":
    main()
