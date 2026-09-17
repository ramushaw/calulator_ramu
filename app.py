import math
import streamlit as st
from machining_data import EN_STEELS, METRIC_FINE_THREADS


# ============================================================
# RAMU ADVANCED MULTI-CALCULATOR CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="RAMU Advanced Multi-Calculator",
    page_icon="⚙️",
    layout="centered"
)


# ============================================================
# APPLICATION HEADER
# ============================================================

st.title("⚙️ RAMU ADVANCED MULTI-CALCULATOR")

st.markdown("### Developed by: **Ramu Shaw**")

st.caption(
    "Pure Python Backend | Streamlit Web Core Engine Interface"
)

st.divider()


# ============================================================
# APPLICATION DESCRIPTION
# ============================================================

st.markdown(
    """
    A comprehensive interactive engineering suite featuring
    four distinct functional domains:

    * **🧮 Arithmetic Matrix:** Complete multi-operational value calculation.
    * **📐 Trigonometric Matrix:** High-precision radian-mapped angular evaluation.
    * **🔩 Threading Engine:** CNC-ready calculation algorithms and Fanuc G76 micron-depth generation.
    * **📚 Engineering Library:** Parameter recall databases for EN Steel stock and ISO Metric Fine parameters.
    """
)


# ============================================================
# ARITHMETIC CALCULATION FUNCTION
# ============================================================

def run_arithmetic(a, b, op):

    if op == "+":
        return a + b

    elif op == "-":
        return a - b

    elif op == "*":
        return a * b

    elif op == "/":
        if b == 0:
            return "It is not permissible"
        else:
            return a / b

    return "Invalid request"


# ============================================================
# MAIN CATEGORY SELECTION
# ============================================================

option = st.selectbox(
    "Choose a calculation category:",
    [
        "Select Category",
        "Arithmetic",
        "Trigonometry",
        "Machining Engine",
        "Engineering Tools & References"
    ]
)


# ============================================================
# 1. ARITHMETIC CALCULATOR
# ============================================================

if option == "Arithmetic":

    st.header("🧮 Arithmetic Calculator")

    val_a = st.number_input(
        "Enter first value (a):",
        value=0.0,
        format="%.4f"
    )

    val_b = st.number_input(
        "Enter second value (b):",
        value=0.0,
        format="%.4f"
    )

    op_select = st.selectbox(
        "Choose operation matrix:",
        ["+", "-", "*", "/"]
    )

    if st.button("Execute Arithmetic Code"):

        outcome = run_arithmetic(
            val_a,
            val_b,
            op_select
        )

        if isinstance(outcome, str):
            st.error(outcome)

        else:
            st.success(
                f"Output Solution: {outcome}"
            )


# ============================================================
# 2. TRIGONOMETRY CALCULATOR
# ============================================================

elif option == "Trigonometry":

    st.header("📐 Trigonometry Calculator")

    deg_input = st.number_input(
        "Enter target angle in degrees:",
        value=0.0,
        format="%.2f"
    )

    func_select = st.selectbox(
        "Select calculation method:",
        [
            "sin",
            "cos",
            "tan",
            "cot",
            "sec",
            "cosec"
        ]
    )

    if st.button("Execute Angular Conversion"):

        # Convert degrees into radians
        rad_scale = math.radians(deg_input)

        try:

            if func_select == "sin":

                st.success(
                    f"sin({deg_input}°) = "
                    f"{math.sin(rad_scale):.4f}"
                )

            elif func_select == "cos":

                st.success(
                    f"cos({deg_input}°) = "
                    f"{math.cos(rad_scale):.4f}"
                )

            elif func_select == "tan":

                st.success(
                    f"tan({deg_input}°) = "
                    f"{math.tan(rad_scale):.4f}"
                )

            elif func_select == "cot":

                if math.isclose(
                    math.tan(rad_scale),
                    0,
                    abs_tol=1e-10
                ):

                    st.error(
                        "Math Exception: Undefined boundary reached."
                    )

                else:

                    st.success(
                        f"cot({deg_input}°) = "
                        f"{(1 / math.tan(rad_scale)):.4f}"
                    )

            elif func_select == "sec":

                if math.isclose(
                    math.cos(rad_scale),
                    0,
                    abs_tol=1e-10
                ):

                    st.error(
                        "Math Exception: Undefined boundary reached."
                    )

                else:

                    st.success(
                        f"sec({deg_input}°) = "
                        f"{(1 / math.cos(rad_scale)):.4f}"
                    )

            elif func_select == "cosec":

                if math.isclose(
                    math.sin(rad_scale),
                    0,
                    abs_tol=1e-10
                ):

                    st.error(
                        "Math Exception: Undefined boundary reached."
                    )

                else:

                    st.success(
                        f"cosec({deg_input}°) = "
                        f"{(1 / math.sin(rad_scale)):.4f}"
                    )

        except Exception:

            st.error(
                "System Error: Angular array computational limits exceeded."
            )


# ============================================================
# 3. MACHINING ENGINE
# ============================================================

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


    # ========================================================
    # 3.1 EN STEEL CUTTING-SPEED INFORMATION
    # ========================================================

    if "1." in sub_select:

        st.subheader(
            "📊 Alloy Surface Velocity Profile"
        )

        target_steel = st.selectbox(
            "Select material designation catalog:",
            list(EN_STEELS.keys())
        )

        s_data = EN_STEELS[target_steel]

        st.markdown(
            f"### **Alloy Parameters: {target_steel}**"
        )

        st.write(
            f"Estimated Carbon Composition: "
            f"**{s_data['carbon']:.2f}%**"
        )

        st.write(
            f"Target Velocity - Uncoated Tool Arrays: "
            f"**{s_data['uncoated_CS']} m/min**"
        )

        st.write(
            f"Target Velocity - Coated Inserts/Carbide: "
            f"**{s_data['coated_CS']} m/min**"
        )

        st.info(
            f"Technical Summary: Optimized machining baseline "
            f"set to {s_data['coated_CS']} m/min."
        )


    # ========================================================
    # 3.2 CS / RPM / DIAMETER CALCULATOR
    # ========================================================

    elif "2." in sub_select:

        st.subheader(
            "⚙️ Dimensional Motion Matrix"
        )

        calc_mode = st.selectbox(
            "Metric to compute:",
            [
                "Cutting Speed (CS)",
                "RPM",
                "Diameter"
            ]
        )


        # ----------------------------------------------------
        # CUTTING SPEED
        # ----------------------------------------------------

        if calc_mode == "Cutting Speed (CS)":

            dia_m = st.number_input(
                "Stock Diameter (mm):",
                min_value=0.0,
                value=0.0
            )

            rpm_m = st.number_input(
                "Spindle Rate (RPM):",
                min_value=0.0,
                value=0.0
            )

            if st.button("Compute Cutting Speed"):

                if dia_m <= 0 or rpm_m <= 0:

                    st.error(
                        "Dimensional inputs must register "
                        "values above zero scale."
                    )

                else:

                    cutting_speed = (
                        3.14 * dia_m * rpm_m
                    ) / 1000

                    st.success(
                        f"Resulting Surface Speed: "
                        f"{cutting_speed:.2f} m/min"
                    )


        # ----------------------------------------------------
        # RPM
        # ----------------------------------------------------

        elif calc_mode == "RPM":

            cs_m = st.number_input(
                "Surface Speed (m/min):",
                min_value=0.0,
                value=0.0
            )

            dia_m = st.number_input(
                "Stock Diameter (mm):",
                min_value=0.0,
                value=0.0
            )

            if st.button("Compute Spindle RPM"):

                if cs_m <= 0 or dia_m <= 0:

                    st.error(
                        "Dimensional inputs must register "
                        "values above zero scale."
                    )

                else:

                    required_rpm = (
                        cs_m * 1000
                    ) / (3.14 * dia_m)

                    st.success(
                        f"Required Target Rotation Speed: "
                        f"{int(required_rpm)} RPM"
                    )


        # ----------------------------------------------------
        # DIAMETER
        # ----------------------------------------------------

        elif calc_mode == "Diameter":

            cs_m = st.number_input(
                "Surface Speed (m/min):",
                min_value=0.0,
                value=0.0
            )

            rpm_m = st.number_input(
                "Spindle Rate (RPM):",
                min_value=0.0,
                value=0.0
            )

            if st.button("Compute Target Diameter"):

                if cs_m <= 0 or rpm_m <= 0:

                    st.error(
                        "Dimensional inputs must register "
                        "values above zero scale."
                    )

                else:

                    target_diameter = (
                        cs_m * 1000
                    ) / (3.14 * rpm_m)

                    st.success(
                        f"Required Stock Dimensional Diameter: "
                        f"{target_diameter:.2f} mm"
                    )


    # ========================================================
    # 3.3 THREADING CALCULATION ENGINE
    # ========================================================

    elif "3." in sub_select:

        st.subheader(
            "🗜️ Unified Thread Calculation Engine"
        )

        st.warning(
            "⚠️ FANUC G76 REFERENCE: "
            "In your stated two-line Fanuc G76 format, "
            "the second-line P value represents single-sided "
            "radial thread depth in microns."
        )

        t_nom = st.number_input(
            "Nominal Thread Outer Major Boundary (mm):",
            min_value=0.0,
            value=12.0
        )

        t_pitch = st.number_input(
            "Thread Thread Pitch Vector (mm):",
            min_value=0.0,
            value=1.75
        )

        if st.button("Analyze Mechanical Thread Array"):

            if t_nom <= 0 or t_pitch <= 0:

                st.error(
                    "Thread parameters must map above "
                    "structural boundaries."
                )

            else:

                # Basic ISO metric external-thread radial depth
                rad_d = 0.61343 * t_pitch

                # Basic theoretical external minor diameter
                min_dia_c = t_nom - (2 * rad_d)

                # Convert radial depth from mm to microns
                radial_depth_micron = rad_d * 1000

                # Four-digit Fanuc P reference
                fanuc_p = int(
                    round(radial_depth_micron)
                )

                st.markdown(
                    "### **Processed Geometric Values**"
                )

                st.write(
                    f"Major Axis Nominal Outer Boundary: "
                    f"**{t_nom:.3f} mm**"
                )

                st.write(
                    f"Declared Profile Matrix Pitch: "
                    f"**{t_pitch:.3f} mm**"
                )

                st.write(
                    f"Radial Thread Height "
                    f"(Single-Side Depth): "
                    f"**{rad_d:.4f} mm**"
                )

                st.write(
                    f"Radial Thread Height: "
                    f"**{radial_depth_micron:.0f} µm**"
                )

                st.write(
                    f"Theoretical Root Minor Structural Core: "
                    f"**{min_dia_c:.4f} mm**"
                )

                st.success(
                    f"🎯 **FANUC G76 SECOND-LINE P REFERENCE:** "
                    f"**P{fanuc_p:04d}**"
                )

                st.caption(
                    "P value shown as four-digit radial thread "
                    "depth in microns according to the Fanuc "
                    "format specified for your machine."
                )


    # ========================================================
    # 3.4 STANDARD METRIC FINE THREAD REFERENCE
    # ========================================================

    elif "4." in sub_select:

        st.subheader(
            "📖 ISO Metric Fine Pitch Structural Library"
        )

        thread_labels = [
            t[0] for t in METRIC_FINE_THREADS
        ]

        selected_label = st.selectbox(
            "Select designated thread scale configuration:",
            thread_labels
        )

        matched_tuple = next(
            t for t in METRIC_FINE_THREADS
            if t[0] == selected_label
        )

        nom_d = matched_tuple[1]
        pt = matched_tuple[2]

        # Basic ISO metric external-thread radial depth
        radial_depth_calculated = 0.61343 * pt

        # Basic theoretical external minor diameter
        minor_d_calculated = (
            nom_d - (2 * radial_depth_calculated)
        )

        # Convert to microns
        radial_depth_micron = (
            radial_depth_calculated * 1000
        )

        # Four-digit Fanuc P reference
        fanuc_p = int(
            round(radial_depth_micron)
        )

        st.markdown(
            f"### **Mechanical Specification Matrix: "
            f"{selected_label}**"
        )

        st.write(
            f"Major Core Axis Nominal Boundary: "
            f"**{nom_d:.2f} mm**"
        )

        st.write(
            f"Profile Thread Pitch Configuration: "
            f"**{pt:.2f} mm**"
        )

        st.write(
            f"Single-Side Radial Depth Profile: "
            f"**{radial_depth_calculated:.4f} mm**"
        )

        st.write(
            f"Radial Thread Depth: "
            f"**{radial_depth_micron:.0f} µm**"
        )

        st.write(
            f"Theoretical Core Minor Boundary Axis: "
            f"**{minor_d_calculated:.4f} mm**"
        )

        st.success(
            f"🎯 **FANUC G76 SECOND-LINE P REFERENCE:** "
            f"**P{fanuc_p:04d}**"
        )

        st.caption(
            "P value represents the calculated single-sided "
            "radial thread depth in microns."
        )


# ============================================================
# 4. ENGINEERING TOOLS & REFERENCES
# ============================================================

elif option == "Engineering Tools & References":

    st.header(
        "🔗 Engineering Tools & References"
    )

    st.markdown(
        """
        Useful external engineering calculators and reference
        tools for specialized tasks that are outside the
        direct calculation functions of RAMU.
        """
    )

    st.divider()


    # ========================================================
    # HARDNESS CONVERSION
    # ========================================================

    st.subheader(
        "🔩 Hardness Conversion"
    )

    st.write(
        "Convert hardness values between Vickers, "
        "Brinell and Rockwell scales."
    )

    st.link_button(
        "🔗 Open Hardness Conversion Calculator",
        "https://www.rivcut.com/resources/hardness-conversion-calculator"
    )


    st.divider()


    # ========================================================
    # TOLERANCE & FIT
    # ========================================================

    st.subheader(
        "📐 Tolerance & Fit Calculator"
    )

    st.write(
        "Calculate and review dimensional tolerances "
        "and engineering fits."
    )

    st.link_button(
        "🔗 Open Tolerance & Fit Calculator",
        "https://www.machiningdoctor.com/calculators/tolerances/#tolerance-fit-calculator"
    )


    st.divider()


    # ========================================================
    # SURFACE FINISH
    # ========================================================

    st.subheader(
        "⚙️ Surface Finish Calculator"
    )

    st.write(
        "Convert and compare surface-finish parameters "
        "using the external reference calculator."
    )

    st.link_button(
        "🔗 Open Surface Finish Calculator",
        "https://www.machiningdoctor.com/calculators/surface-finish-calculator/#surface-finish-conversion-chart"
    )


# ============================================================
# APPLICATION FOOTER
# ============================================================

st.divider()

st.caption(
    "RAMU Advanced Multi-Calculator | "
    "Engineering Calculation & Reference Platform"
)
