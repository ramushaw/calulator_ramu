import streamlit as st
import math

# Set up the title of the web app
st.title("Advanced Multi-Calculator made by Ramu Shaw")
st.write("Perform Arithmetic, Trigonometry, or Machining calculations in one place.")

# Dropdown menu for the main calculation category
option = st.selectbox(
    "Choose a calculation category:", 
    ["Select an option", "Arithmetic", "Trigonometry", "Machining"]
)

# ---------------- ARITHMETIC ----------------
if option == "Arithmetic":
    st.header("🧮 Arithmetic Calculator")
    
    a = st.number_input("Please enter first number:", format="%.4f")
    b = st.number_input("Please enter second number:", format="%.4f")
    operation = st.selectbox("Choose operation:", ["+", "-", "*", "/"])
    
    if st.button("Calculate Arithmetic"):
        if operation == "+":
            st.success(f"The answer is: {a + b}")
        elif operation == "-":
            st.success(f"The answer is: {a - b}")
        elif operation == "*":
            st.success(f"The answer is: {a * b}")
        elif operation == "/":
            if b == 0:
                st.error("It is not permissible (Division by zero)")
            else:
                st.success(f"The answer is: {a / b}")

# ---------------- TRIGONOMETRY ----------------
elif option == "Trigonometry":
    st.header("📐 Trigonometry Calculator")
    
    degree = st.number_input("Please enter the angle in degrees:", format="%.2f")
    function = st.selectbox("Choose function:", ["sin", "cos", "tan", "cot", "sec", "cosec"])
    
    if st.button("Calculate Trigonometry"):
        try:
            radians = math.radians(degree)
            if function == "sin":
                ans = math.sin(radians)
            elif function == "cos":
                ans = math.cos(radians)
            elif function == "tan":
                ans = math.tan(radians)
            elif function == "cot":
                ans = 1 / math.tan(radians)
            elif function == "sec":
                ans = 1 / math.cos(radians)
            elif function == "cosec":
                ans = 1 / math.sin(radians)
                
            st.success(f"{function} ({degree}°) = {ans:.4f}")
        except ZeroDivisionError:
            st.error(f"Math Error: {function} is undefined for {degree}°")

# ---------------- MACHINING ----------------
elif option == "Machining":
    st.header("🔧 Machining Calculator")
    
    choice = st.selectbox("What do you want to calculate?", ["Select an option", "CS", "RPM", "Diameter"])
    
    if choice == "CS":
        diameter = st.number_input("Enter diameter in mm:", min_value=0.0, format="%.2f")
        rpm = st.number_input("Enter RPM:", min_value=0.0, format="%.2f")
        
        if st.button("Calculate Cutting Speed"):
            if diameter > 0 and rpm > 0:
                answer = (3.14 * diameter * rpm) / 1000
                st.success(f"The cutting speed is {answer:.2f} m/min")
            else:
                st.error("Please enter values greater than zero.")
                
    elif choice == "RPM":
        cs = st.number_input("Enter cutting speed in m/min:", min_value=0.0, format="%.2f")
        diameter = st.number_input("Enter diameter in mm:", min_value=0.0, format="%.2f")
        
        if st.button("Calculate RPM"):
            if cs > 0 and diameter > 0:
                answer = (cs * 1000) / (3.14 * diameter)
                st.success(f"The required RPM is {answer:.0f}")
            else:
                st.error("Please enter values greater than zero.")
                
    elif choice == "Diameter":
        cs = st.number_input("Enter cutting speed in m/min:", min_value=0.0, format="%.2f")
        rpm = st.number_input("Enter RPM:", min_value=0.0, format="%.2f")
        
        if st.button("Calculate Diameter"):
            if cs > 0 and rpm > 0:
                answer = (cs * 1000) / (3.14 * rpm)
                st.success(f"The required diameter is {answer:.2f} mm")
            else:
                st.error("Please enter values greater than zero.")
