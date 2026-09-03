import math
import streamlit as st

# ============================================================
# RAMU ADVANCED MULTI-CALCULATOR CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="RAMU Advanced Multi-Calculator",
    page_icon="⚙️",
    layout="centered"
)

# Custom header highlighting your profile
st.title("⚙️ RAMU ADVANCED MULTI-CALCULATOR")
st.markdown("### Developed by: **Ramu Shaw**")
st.caption("Pure Python Backend | Streamlit Web Core Engine Interface")
st.divider()

st.markdown(
    """
    A comprehensive interactive engineering suite featuring four distinct functional domains:
    * **🧮 Arithmetic Matrix:** Complete multi-operational value calculation.
    * **📐 Trigonometric Matrix:** High-precision radian-mapped angular evaluation.
    * **🔩 Threading Engine:** CNC-ready calculation algorithms and **Fanuc G76** micron-depth generation.
    * **📚 Engineering Library:** Instant parameter recall databases for EN Steel stock and ISO Metric Fine parameters.
    """
)

# ============================================================
# EN STEEL ALLOY DATABASE
# ============================================================
EN_STEELS = {
    "EN8": {"carbon": 0.40, "uncoated_CS": 140, "coated_CS": 215},
    "EN9": {"carbon": 0.55, "uncoated_CS": 120, "coated_CS": 170},
    "EN19": {"carbon": 0.40, "uncoated_CS": 110, "coated_CS": 165},
    "EN24": {"carbon": 0.40, "uncoated_CS": 100, "coated_CS": 135},
    "EN30B": {"carbon": 0.30, "uncoated_CS": 90, "coated_CS": 125},
    "EN36B": {"carbon": 0.15, "uncoated_CS": 140, "coated_CS": 190},
    "EN36K": {"carbon": 0.15, "uncoated_CS": 140, "coated_CS": 190},
    "EN56C": {"carbon": 0.21, "uncoated_CS": 110, "coated_CS": 155},
    "EN42": {"carbon": 0.65, "uncoated_CS": 110, "coated_CS": 145}
}

# ============================================================
# ISO METRIC FINE PITCH CATALOG
# ============================================================
METRIC_FINE_THREADS = [
    ("M1.6 × 0.20", 1.6, 0.20), ("M2 × 0.25", 2.0, 0.25), ("M2.5 × 0.35", 2.5, 0.35),
    ("M3 × 0.35", 3.0, 0.35), ("M4 × 0.50", 4.0, 0.50), ("M5 × 0.50", 5.0, 0.50),
    ("M6 × 0.75", 6.0, 0.75), ("M8 × 1.00", 8.0, 1.00), ("M8 × 0.75", 8.0, 0.75),
    ("M10 × 1.25", 10.0, 1.25), ("M10 × 1.00", 10.0, 1.00), ("M10 × 0.75", 10.0, 0.75),
    ("M12 × 1.50", 12.0, 1.50), ("M12 × 1.25", 12.0, 1.25), ("M14 × 1.50", 14.0, 1.50),
    ("M16 × 1.50", 16.0, 1.50), ("M18 × 2.00", 18.0, 2.00), ("M18 × 1.50", 18.0, 1.50),
    ("M20 × 2.00", 20.0, 2.00), ("M20 × 1.50", 20.0, 1.50), ("M22 × 2.00", 22.0, 2.00),
    ("M22 × 1.50", 22.0, 1.50), ("M24 × 2.00", 24.0, 2.00), ("M27 × 2.00", 27.0, 2.00),
    ("M30 × 2.00", 30.0, 2.00), ("M33 × 2.00", 33.0, 2.00), ("M36 × 3.00", 36.0, 3.00),
    ("M39 × 3.00", 39.0, 3.00), ("M42 × 3.00", 42.0, 3.00), ("M45 × 3.00", 45.0, 3.00),
    ("M48 × 3.00", 48.0, 3.00), ("M52 × 4.00", 52.0, 4.00), ("M56 × 4.00", 56.0, 4.00),
    ("M60 × 4.00", 60.0, 4.00), ("M64 × 4.00", 64.0, 4.00)
]

# ============================================================
# UTILITY HELPER LOGIC
# ============================================================
def run_arithmetic(a, b, op):
    if op == "+": return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b
    elif op == "/": return "It is not permissible" if b == 0 else a / b
    return "Invalid request"

# ============================================================
# PRIMARY CORE DIVISION ROUTING
# ============================================================
option = st.selectbox(
    "Choose a calculation category:",
    ["Select Category", "Arithmetic", "Trigonometry", "Machining Engine"]
)

# ------------------------------------------------------------
# MODULE 1: ARITHMETIC CONSOLE
# ------------------------------------------------------------
if option == "Arithmetic":
    st.header("🧮 Arithmetic Calculator")
    val_a = st.number_input("Enter first value (a):", value=0.0, format="%.4f")
    val_b = st.number_input("Enter second value (b):", value=0.0, format="%.4f")
    op_select = st.selectbox("Choose operation matrix:", ["+", "-", "*", "/"])
    
    if st.button("Execute Arithmetic Code"):
        outcome = run_arithmetic(val_a, val_b, op_select)
        if isinstance(outcome, str): st.error(outcome)
        else: st.success(f"Output Solution: {outcome}")

# ------------------------------------------------------------
# MODULE 2: TRIGONOMETRIC CONSOLE
# ------------------------------------------------------------
elif option == "Trigonometry":
    st.header("📐 Trigonometry Calculator")
    deg_input = st.number_input("Enter target angle in degrees:", value=0.0, format="%.2f")
    func_select = st.selectbox("Select calculation method:", ["sin", "cos", "tan", "cot", "sec", "cosec"])
    
    if st.button("Execute Angular Conversion"):
        rad_scale = math.radians(deg_input)
        try:
            if func_select == "sin": st.success(f"sin({deg_input}°) = {math.sin(rad_scale):.4f}")
            elif func_select == "cos": st.success(f"cos({deg_input}°) = {math.cos(rad_scale):.4f}")
            elif func_select == "tan": st.success(f"tan({deg_input}°) = {math.tan(rad_scale):.4f}")
            elif func_select == "cot":
                if math.isclose(math.tan(rad_scale), 0, abs_tol=1e-10): st.error("Math Exception: Undefined boundary reached.")
                else: st.success(f"cot({deg_input}°) = {(1 / math.tan(rad_scale)):.4f}")
            elif func_select == "sec":
                if math.isclose(math.cos(rad_scale), 0, abs_tol=1e-10): st.error("Math Exception: Undefined boundary reached.")
                else: st.success(f"sec({deg_input}°) = {(1 / math.cos(rad_scale)):.4f}")
            elif func_select == "cosec":
                if math.isclose(math.sin(rad_scale), 0, abs_tol=1e-10): st.error("Math Exception: Undefined boundary reached.")
                else: st.success(f"cosec({deg_input}°) = {(1 / math.sin(rad_scale)):.4f}")
        except Exception:
            st.error("System Error: Angular array computational limits exceeded.")

# ------------------------------------------------------------
# MODULE 3: MACHINING CONSOLE
# ------------------------------------------------------------
elif option == "Machining Engine":
    st.header("🔧 Industrial Machining Systems")
    sub_select = st.selectbox(
        "Choose targeted industrial tool suite:",
        [
            "Select sub-system",
            "1. EN Steel Cutting-Speed Information",
            "2. CS / RPM / Diameter Calculator",
            "3. Threading Calculation Engine",
            "4. Standard Metric Fine Thread Reference"
        ]
    )

    # 3.1: EN STOCK METALLURGY DATA
    if "1." in sub_select:
        st.subheader("📊 Alloy Surface Velocity Profile")
        target_steel = st.selectbox("Select material designation catalog:", list(EN_STEELS.keys()))
        s_data = EN_STEELS[target_steel]
        
        st.markdown(f"### **Alloy Parameters: {target_steel}**")
        st.write(f"Estimated Carbon Composition: **{s_data['carbon']:.2f}%**")
        st.write(f"Target Velocity - Uncoated Tool Arrays: **{s_data['uncoated_CS']} m/min**")
        st.write(f"Target Velocity - Coated Inserts/Carbide: **{s_data['coated_CS']} m/min**")
        st.info(f"Technical Summary: Optimized machining baseline set to {s_data['coated_CS']} m/min.")

    # 3.2: ROTATIONAL SPEEDS & VECTOR DATA
    elif "2." in sub_select:
        st.subheader("⚙️ Dimensional Motion Matrix")
        calc_mode = st.selectbox("Metric to compute:", ["Cutting Speed (CS)", "RPM", "Diameter"])
        
        if calc_mode == "Cutting Speed (CS)":
            dia_m = st.number_input("Stock Diameter (mm):", min_value=0.0, value=0.0)
            rpm_m = st.number_input("Spindle Rate (RPM):", min_value=0.0, value=0.0)
            if st.button("Compute Cutting Speed"):
                if dia_m <= 0 or rpm_m <= 0: st.error("Dimensional inputs must register values above zero scale.")
                else: st.success(f"Resulting Surface Speed: {((3.14 * dia_m * rpm_m) / 1000):.2f} m/min")
                
        elif calc_mode == "RPM":
            cs_m = st.number_input("Surface Speed (m/min):", min_value=0.0, value=0.0)
            dia_m = st.number_input("Stock Diameter (mm):", min_value=0.0, value=0.0)
            if st.button("Compute Spindle RPM"):
                if cs_m <= 0 or dia_m <= 0: st.error("Dimensional inputs must register values above zero scale.")
                else: st.success(f"Required Target Rotation Speed: {int((cs_m * 1000) / (3.14 * dia_m))} RPM")
                
        elif calc_mode == "Diameter":
            cs_m = st.number_input("Surface Speed (m/min):", min_value=0.0, value=0.0)
            rpm_m = st.number_input("Spindle Rate (RPM):", min_value=0.0, value=0.0)
            if st.button("Compute Target Diameter"):
                if cs_m <= 0 or rpm_m <= 0: st.error("Dimensional inputs must register values above zero scale.")
                else: st.success(f"Required Stock Dimensional Diameter: {((cs_m * 1000) / (3.14 * rpm_m)):.2f} mm")

    # 3.3: HARD THREADING G76 PROCESSOR
    elif "3." in sub_select:
        st.subheader("🗜️ Unified Thread Calculation Engine")
        st.warning(
            "⚠️ REGULATORY COMPLIANCE: The generated G76 P-value layout directly satisfies Fanuc "
            "two-block microcode formatting where block-two P arguments require absolute single-sided "
            "radial structural thread depths explicitly scaled in microns."
        )
        t_nom = st.number_input("Nominal Thread Outer Major Boundary (mm):", min_value=0.0, value=12.0)
        t_pitch = st.number_input("Thread Thread Pitch Vector (mm):", min_value=0.0, value=1.75)
        
        if st.button("Analyze Mechanical Thread Array"):
            if t_nom <= 0 or t_pitch <= 0: st.error("Thread parameters must map above structural boundaries.")
            else:
