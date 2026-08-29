import math
import streamlit as st


# ============================================================
# RAMU ADVANCED MULTI-CALCULATOR
# ============================================================

st.set_page_config(
    page_title="RAMU Advanced Multi-Calculator",
    page_icon="🧮",
    layout="centered"
)


# ============================================================
# TITLE AND DESCRIPTION
# ============================================================

st.title("RAMU Advanced Multi-Calculator")

st.write(
    "A practical calculator for Arithmetic, Trigonometry, and "
    "Machining calculations, with quick EN-steel cutting-speed "
    "reference data for coated and uncoated carbide tooling."
)


# ============================================================
# EN STEEL DATABASE
# ============================================================

EN_STEELS = {

    "EN8": {
        "carbon": 0.40,
        "uncoated_CS": 140,
        "coated_CS": 215
    },

    "EN9": {
        "carbon": 0.55,
        "uncoated_CS": 120,
        "coated_CS": 170
    },

    "EN19": {
        "carbon": 0.40,
        "uncoated_CS": 110,
        "coated_CS": 165
    },

    "EN24": {
        "carbon": 0.40,
        "uncoated_CS": 100,
        "coated_CS": 135
    },

    "EN30B": {
        "carbon": 0.30,
        "uncoated_CS": 90,
        "coated_CS": 125
    },

    "EN36B": {
        "carbon": 0.15,
        "uncoated_CS": 140,
        "coated_CS": 190
    },

    "EN36K": {
        "carbon": 0.15,
        "uncoated_CS": 140,
        "coated_CS": 190
    },

    "EN56C": {
        "carbon": 0.21,
        "uncoated_CS": 110,
        "coated_CS": 155
    },

    "EN42": {
        "carbon": 0.65,
        "uncoated_CS": 110,
        "coated_CS": 145
    }
}


# ============================================================
# ARITHMETIC FUNCTION
# ============================================================

def calculate(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":

        if b == 0:
            return "It is not permissible"

        else:
            return a / b

    else:
        return "Invalid request"


# ============================================================
# MAIN CATEGORY
# ============================================================

option = st.selectbox(
    "Choose a calculation category:",
    [
        "Arithmetic",
        "Trigonometry",
        "Machining"
    ]
)


# ============================================================
# ARITHMETIC
# ============================================================

if option == "Arithmetic":

    st.subheader("Arithmetic Calculator")

    a = st.number_input(
        "Enter first number:",
        value=0.0
    )

    b = st.number_input(
        "Enter second number:",
        value=0.0
    )

    operation = st.selectbox(
        "Choose operation:",
        ["+", "-", "*", "/"]
    )

    if st.button("Calculate", key="arithmetic_button"):

        answer = calculate(a, b, operation)

        if isinstance(answer, str):
            st.error(answer)
        else:
            st.success(f"The answer is {answer}")


# ============================================================
# TRIGONOMETRY
# ============================================================

elif option == "Trigonometry":

    st.subheader("Trigonometry Calculator")

    degree = st.number_input(
        "Enter angle in degrees:",
        value=0.0
    )

    function = st.selectbox(
        "Choose trigonometric function:",
        [
            "sin",
            "cos",
            "tan",
            "cot",
            "sec",
            "cosec"
        ]
    )

    if st.button("Calculate", key="trigonometry_button"):

        radian = math.radians(degree)

        if function == "sin":

            answer = math.sin(radian)
            st.success(f"sin {degree}° = {answer:.4f}")

        elif function == "cos":

            answer = math.cos(radian)
            st.success(f"cos {degree}° = {answer:.4f}")

        elif function == "tan":

            answer = math.tan(radian)
            st.success(f"tan {degree}° = {answer:.4f}")

        elif function == "cot":

            if math.isclose(
                math.tan(radian),
                0,
                abs_tol=1e-10
            ):
                st.error("cot is undefined at this angle.")

            else:
                answer = 1 / math.tan(radian)
                st.success(f"cot {degree}° = {answer:.4f}")

        elif function == "sec":

            if math.isclose(
                math.cos(radian),
                0,
                abs_tol=1e-10
            ):
                st.error("sec is undefined at this angle.")

            else:
                answer = 1 / math.cos(radian)
                st.success(f"sec {degree}° = {answer:.4f}")

        elif function == "cosec":

            if math.isclose(
                math.sin(radian),
                0,
                abs_tol=1e-10
            ):
                st.error("cosec is undefined at this angle.")

            else:
                answer = 1 / math.sin(radian)
                st.success(f"cosec {degree}° = {answer:.4f}")


# ============================================================
# MACHINING
# ============================================================

elif option == "Machining":

    st.subheader("Machining Calculator")

    machining_option = st.selectbox(
        "Choose machining calculation:",
        [
            "EN Steel Cutting-Speed Information",
            "CS / RPM / Diameter Calculator"
        ]
    )


    # ========================================================
    # EN STEEL INFORMATION
    # ========================================================

    if machining_option == "EN Steel Cutting-Speed Information":

        st.write(
            "Reference data for selected EN steels."
        )

        steel = st.selectbox(
            "Choose EN steel:",
            list(EN_STEELS.keys())
        )

        data = EN_STEELS[steel]

        st.subheader(f"{steel} — Reference Information")

        st.write(
            f"Average carbon content: "
            f"**{data['carbon']:.2f}%**"
        )

        st.write(
            f"Recommended CS with uncoated carbide: "
            f"**{data['uncoated_CS']} m/min**"
        )

        st.write(
            f"Recommended CS with coated carbide / insert: "
            f"**{data['coated_CS']} m/min**"
        )

        st.info(
            f"For {steel}, reference cutting speed is approximately "
            f"**{data['coated_CS']} m/min** with coated carbide "
            f"and **{data['uncoated_CS']} m/min** with uncoated carbide."
        )

        st.caption(
            "Cutting-speed values are reference values and should "
            "be selected according to actual tooling, operation, "
            "workpiece condition and machining conditions."
        )


    # ========================================================
    # NORMAL MACHINING CALCULATOR
    # ========================================================

    elif machining_option == "CS / RPM / Diameter Calculator":

        choice = st.selectbox(
            "What do you want to calculate?",
            [
                "Cutting Speed (CS)",
                "RPM",
                "Diameter"
            ]
        )


        # ====================================================
        # CUTTING SPEED
        # ====================================================

        if choice == "Cutting Speed (CS)":

            diameter = st.number_input(
                "Enter diameter in mm:",
                min_value=0.0,
                value=0.0
            )

            rpm = st.number_input(
                "Enter RPM:",
                min_value=0.0,
                value=0.0
            )

            if st.button(
                "Calculate Cutting Speed",
                key="cs_button"
            ):
                if diameter <= 0 or rpm <= 0:
                    st.error("Please enter values greater than zero.")
                else:
                    answer = (3.14 * diameter * rpm) / 1000
                    st.success(f"The cutting speed is {answer:.2f} m/min")

        # ====================================================
        # RPM
        # ====================================================

        elif choice == "RPM":

            cs = st.number_input(
                "Enter cutting speed in m/min:",
                min_value=0.0,
                value=0.0
            )

            diameter = st.number_input(
                "Enter diameter in mm:",
                min_value=0.0,
                value=0.0
            )

            if st.button(
                "Calculate RPM",
                key="rpm_button"
            ):
                if cs <= 0 or diameter <= 0:
                    st.error("Please enter values greater than zero.")
                else:
                    answer = (cs * 1000) / (3.14 * diameter)
                    st.success(f"The required RPM is {answer:.0f}")

        # ====================================================
        # DIAMETER
        # ====================================================

        elif choice == "Diameter":

            cs = st.number_input(
                "Enter cutting speed in m/min:",
                min_value=0.0,
                value=0.0
            )

            rpm = st.number_input(
                "Enter RPM:",
                min_value=0.0,
                value=0.0
            )

            if st.button(
                "Calculate Diameter",
                key="diameter_button"
            ):
                if cs <= 0 or rpm <= 0:
                    st.error("Please enter values greater than zero.")
                else:
