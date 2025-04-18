import streamlit as st
import base64
import pandas as pd

def background_image(image_file):
    img = get_img_as_base64(image_file)
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: bottom center;
        background-repeat: no-repeat;
    }}
    /* Sidebar width */
    [data-testid="stSidebar"] > div:first-child {{
        width: 260px;
    }}
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Page Configuration ---
st.set_page_config(page_title="Exploring Chemistry", layout="wide")

# --- Utility to load background image ---
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load and set background
background_image("background2.png")

# --- Sidebar Navigation via Buttons ---
st.sidebar.markdown("""
    <div style="text-align:center; margin-top:10px;">
        <h1 style="font-size:50px; margin-bottom:10px;">🔍Menu</h1>
        <p style="font-size:18px; color:#bbb;">Navigate to different sections here!</p>
    </div>
    """,
    unsafe_allow_html=True
)


 # title("🔬 Menu"))

st.sidebar.header("")
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Each button sets the page
if st.sidebar.button("🏠 Home", key='btn_home'):
    st.session_state.page = 'Home'
if st.sidebar.button("⚗️ Chemical Reactions", key='btn_reactions'):
    st.session_state.page = 'Chemical Reactions'
if st.sidebar.button("🔢 Periodic Table", key='btn_table'):
    st.session_state.page = 'Periodic Table'
if st.sidebar.button("📈 Periodic Trends", key='btn_trends'):
    st.session_state.page = 'Periodic Trends'
if st.sidebar.button("🧪 Molecular Structures", key='btn_struct'):
    st.session_state.page = 'Molecular Structures'
if st.sidebar.button("🧮 Stoichiometry", key='btn_stoich'):
    st.session_state.page = 'Stoichiometry'
if st.sidebar.button("🔬 Spectroscopy", key='btn_spec'):
    st.session_state.page = 'Spectroscopy'

# Determine current page
key = st.session_state.page

# --- Page Content ---
if key == 'Home':
    background_image("home_bg.png")
    st.markdown("<h1 style='font-size: 70px;'>Exploring Chemistry!</h1>", unsafe_allow_html=True)
    st.subheader("")
    st.subheader(
        "Welcome to the interactive chemistry exploration app! Here you can learn about chemical reactions, explore the periodic table, visualize trends, and more. Use the sidebar buttons to navigate."
    )

# --- [Existing code before this section remains the same] ---

elif key == 'Chemical Reactions':
    # --- Reaction Data ---
    # [Your extensive reaction_data dictionary remains unchanged here]
    reaction_data = {
        # Precipitation Reactions
        ("Sodium Chloride (NaCl)", "Silver Nitrate (AgNO3)"): {
            "product": "Silver Chloride (AgCl) + Sodium Nitrate (NaNO3)",
            "state": "precipitate + aqueous",
            "color": "white + colorless solution",
            "reaction_type": "precipitation",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Silver_chloride_precipitate.jpg/220px-Silver_chloride_precipitate.jpg"
        },
        ("Barium Chloride (BaCl2)", "Sodium Sulfate (Na2SO4)"): {
            "product": "Barium Sulfate (BaSO4) + Sodium Chloride (NaCl)",
            "state": "precipitate + aqueous",
            "color": "white + colorless solution",
            "reaction_type": "precipitation",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Barium_sulfate_precipitate.jpg/220px-Barium_sulfate_precipitate.jpg"
        },
        ("Barium Chloride (BaCl2)", "Copper(II) Sulfate (CuSO4)"): {
            "product": "Barium Sulfate (BaSO4) + Copper(II) Chloride (CuCl2)",
            "state": "precipitate + aqueous",
            "color": "white + blue solution",
            "reaction_type": "precipitation",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Barium_sulfate_precipitate.jpg/220px-Barium_sulfate_precipitate.jpg"
            # Barium Sulfate precipitate image
        },
        ("Barium Chloride (BaCl2)", "Silver Nitrate (AgNO3)"): {
            "product": "Silver Chloride (AgCl) + Barium Nitrate (Ba(NO3)2)",
            "state": "precipitate + aqueous",
            "color": "white + colorless solution",
            "reaction_type": "precipitation",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Silver_chloride_precipitate.jpg/220px-Silver_chloride_precipitate.jpg"
            # Silver Chloride precipitate image
        },
        ("Copper(II) Sulfate (CuSO4)", "Sodium Hydroxide (NaOH)"): {
            "product": "Copper(II) Hydroxide (Cu(OH)2) + Sodium Sulfate (Na2SO4)",
            "state": "precipitate + aqueous",
            "color": "blue + colorless solution",
            "reaction_type": "precipitation",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Copper_hydroxide_precipitate.jpg/220px-Copper_hydroxide_precipitate.jpg"
        },
        ("Copper(II) Sulfate (CuSO4)", "Ammonia (NH3)"): {  # Initial reaction, excess NH3 forms complex
            "product": "Copper(II) Hydroxide (Cu(OH)2) + Ammonium Sulfate ((NH4)2SO4)",
            "state": "precipitate + aqueous",
            "color": "blue + colorless solution",
            "reaction_type": "precipitation / complex formation (with excess)",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Copper_hydroxide_precipitate.jpg/220px-Copper_hydroxide_precipitate.jpg"
            # Initial precipitate
        },
        ("Silver Nitrate (AgNO3)", "Sodium Hydroxide (NaOH)"): {
            "product": "Silver Oxide (Ag2O) + Sodium Nitrate (NaNO3) + Water (H2O)",  # AgOH decomposes
            "state": "precipitate + aqueous + liquid",
            "color": "brown/black + colorless solution",
            "reaction_type": "precipitation",
            "image": None # Placeholder, Silver Oxide precipitate image needed (Using None for clarity)
        },
        ("Calcium Carbonate (CaCO3)", "Silver Nitrate (AgNO3)"): {  # Note: CaCO3 is poorly soluble
            "product": "Silver Carbonate (Ag2CO3) + Calcium Nitrate (Ca(NO3)2)",
            "state": "precipitate + aqueous",
            "color": "white/pale yellow + colorless solution",
            "reaction_type": "precipitation",
            "image": None # Placeholder, Silver Carbonate precipitate image needed
        },

        # Gas‐evolution / Acid-Base / Single Displacement with Gas
        ("Calcium Carbonate (CaCO3)", "Hydrochloric Acid (HCl)"): {
            "product": "Calcium Chloride (CaCl2) + Water (H2O) + Carbon Dioxide (CO2)",
            "state": "aqueous + liquid + gas",
            "color": "colorless solution + colorless gas",
            "reaction_type": "gas evolution (acid-carbonate)",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Vinegar_and_baking_soda_reaction.jpg/220px-Vinegar_and_baking_soda_reaction.jpg"
            # Example CO2 evolution
        },
        ("Sodium Bicarbonate (NaHCO3)", "Hydrochloric Acid (HCl)"): {
            "product": "Sodium Chloride (NaCl) + Water (H2O) + Carbon Dioxide (CO2)",
            "state": "aqueous + liquid + gas",
            "color": "colorless solution + colorless gas",
            "reaction_type": "gas evolution (acid-bicarbonate)",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Vinegar_and_baking_soda_reaction.jpg/220px-Vinegar_and_baking_soda_reaction.jpg"
            # Example CO2 evolution
        },
        ("Zinc (Zn)", "Hydrochloric Acid (HCl)"): {
            "product": "Zinc Chloride (ZnCl2) + Hydrogen (H2)",
            "state": "aqueous + gas",
            "color": "colorless solution + colorless gas",
            "reaction_type": "single displacement / gas evolution",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Zn_HCl_reaction.jpg/220px-Zn_HCl_reaction.jpg"
        },
        ("Magnesium (Mg)", "Hydrochloric Acid (HCl)"): {
            "product": "Magnesium Chloride (MgCl2) + Hydrogen (H2)",
            "state": "aqueous + gas",
            "color": "colorless solution + colorless gas",
            "reaction_type": "single displacement / gas evolution",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Magnesium_reacting_with_acid.jpg/220px-Magnesium_reacting_with_acid.jpg"
        },
        ("Iron (Fe)", "Hydrochloric Acid (HCl)"): {
            "product": "Iron(II) Chloride (FeCl2) + Hydrogen (H2)",
            "state": "aqueous + gas",
            "color": "pale green solution + colorless gas",
            "reaction_type": "single displacement / gas evolution",
            "image": None # Placeholder, Iron in HCl image needed
        },
        ("Ammonia (NH3)", "Hydrochloric Acid (HCl)"): {  # Reaction between gases
            "product": "Ammonium Chloride (NH4Cl)",
            "state": "solid (fine white smoke)",
            "color": "white",
            "reaction_type": "acid‑base gas reaction / combination",
            "image": "ammonium_chloride.png"
        },

        # Neutralization (Acid-Base without gas)
        ("Sodium Hydroxide (NaOH)", "Hydrochloric Acid (HCl)"): {
            "product": "Sodium Chloride (NaCl) + Water (H2O)",
            "state": "aqueous + liquid",
            "color": "colorless",
            "reaction_type": "neutralization",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Water_drop.jpg/220px-Water_drop.jpg"
            # Water image as placeholder
        },

        # Single‐displacement (Metal displacement)
        ("Copper (Cu)", "Silver Nitrate (AgNO3)"): {
            "product": "Copper(II) Nitrate (Cu(NO3)2) + Silver (Ag)",
            "state": "aqueous + solid",
            "color": "blue solution + metallic gray solid",
            "reaction_type": "single displacement",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Silver_nitrate_copper.jpg/220px-Silver_nitrate_copper.jpg"
        },
        ("Zinc (Zn)", "Silver Nitrate (AgNO3)"): {
            "product": "Zinc Nitrate (Zn(NO3)2) + Silver (Ag)",
            "state": "aqueous + solid",
            "color": "colorless solution + metallic gray solid",
            "reaction_type": "single displacement",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Silver_nitrate_copper.jpg/220px-Silver_nitrate_copper.jpg"
            # Similar visual effect (metal deposition)
        },
        ("Magnesium (Mg)", "Silver Nitrate (AgNO3)"): {
            "product": "Magnesium Nitrate (Mg(NO3)2) + Silver (Ag)",
            "state": "aqueous + solid",
            "color": "colorless solution + metallic gray solid",
            "reaction_type": "single displacement",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Silver_nitrate_copper.jpg/220px-Silver_nitrate_copper.jpg"
            # Similar visual effect (metal deposition)
        },
        ("Iron (Fe)", "Silver Nitrate (AgNO3)"): {
            "product": "Iron(II) Nitrate (Fe(NO3)2) + Silver (Ag)",
            "state": "aqueous + solid",
            "color": "pale green solution + metallic gray solid",
            "reaction_type": "single displacement",
            "image": None # Placeholder, Iron in AgNO3 image needed
        },
        ("Zinc (Zn)", "Copper(II) Sulfate (CuSO4)"): {
            "product": "Zinc Sulfate (ZnSO4) + Copper (Cu)",
            "state": "aqueous + solid",
            "color": "colorless solution + reddish‑brown solid",
            "reaction_type": "single displacement",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Zinc_in_copper_sulfate.jpg/220px-Zinc_in_copper_sulfate.jpg"
        },
        ("Magnesium (Mg)", "Copper(II) Sulfate (CuSO4)"): {
            "product": "Magnesium Sulfate (MgSO4) + Copper (Cu)",
            "state": "aqueous + solid",
            "color": "colorless solution + reddish‑brown solid",
            "reaction_type": "single displacement",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Copper_sulfate_with_iron_nails.jpg/220px-Copper_sulfate_with_iron_nails.jpg"
            # Similar visual effect
        },
        ("Iron (Fe)", "Copper(II) Sulfate (CuSO4)"): {
            "product": "Iron(II) Sulfate (FeSO4) + Copper (Cu)",
            "state": "aqueous + solid",
            "color": "pale green solution + reddish‑brown solid",
            "reaction_type": "single displacement",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Fe_CuSO4_reaction.jpg/220px-Fe_CuSO4_reaction.jpg"
        },

        # Combination (Synthesis)
        ("Hydrogen (H2)", "Oxygen (O2)"): {  # Requires ignition/catalyst
            "product": "Water (H2O)",
            "state": "liquid/gas",
            "color": "colorless",
            "reaction_type": "combination / combustion",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Water_drop.jpg/220px-Water_drop.jpg"
            # Water image
        },
        ("Magnesium (Mg)", "Oxygen (O2)"): {  # Requires ignition (burning)
            "product": "Magnesium Oxide (MgO)",
            "state": "solid",
            "color": "white (bright light during reaction)",
            "reaction_type": "combination / combustion",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Magnesium_burn.jpg/220px-Magnesium_burn.jpg"
        },
        ("Iron (Fe)", "Oxygen (O2)"): {  # Rusting, requires water/time
            "product": "Iron(III) Oxide (Fe2O3)",
            "state": "solid",
            "color": "reddish-brown",
            "reaction_type": "combination / oxidation (rusting)",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Rust_on_iron.jpg/220px-Rust_on_iron.jpg"
        },
        ("Copper (Cu)", "Oxygen (O2)"): {  # Requires heating
            "product": "Copper(II) Oxide (CuO)",
            "state": "solid",
            "color": "black",
            "reaction_type": "combination / oxidation",
            "image": None # Placeholder, Oxidized copper image needed
        },
        ("Zinc (Zn)", "Oxygen (O2)"): {  # Requires heating
            "product": "Zinc Oxide (ZnO)",
            "state": "solid",
            "color": "white (yellow when hot)",
            "reaction_type": "combination / oxidation",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Zinc_Oxide.jpg/220px-Zinc_Oxide.jpg"
        },

        # Decomposition
        ("Hydrogen Peroxide (H2O2)", "Manganese Dioxide (MnO2)"): {  # MnO2 acts as catalyst
            "product": "Water (H2O) + Oxygen (O2)",
            "state": "liquid + gas",
            "color": "colorless liquid + colorless gas",
            "reaction_type": "decomposition (catalyzed)",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/H2O2_decomposition.jpg/220px-H2O2_decomposition.jpg"
        }
    }

    # --- Reactant Options ---
    all_reactants = set()
    for r1, r2 in reaction_data.keys():
        all_reactants.add(r1)
        all_reactants.add(r2)

    reactant_list = sorted(list(all_reactants))
    reactant_options = ["---Select---"] + reactant_list

    # --- Session State Initialization ---
    if 'reactant1' not in st.session_state:
        st.session_state.reactant1 = reactant_options[0]
    if 'reactant2' not in st.session_state:
        st.session_state.reactant2 = reactant_options[0]
    if 'product_info' not in st.session_state:
        st.session_state.product_info = None
    if 'show_placeholder' not in st.session_state:
        st.session_state.show_placeholder = True
    if 'error_message' not in st.session_state: # Added state for error messages
        st.session_state.error_message = None

    # --- UI ---
    st.markdown("<h1 style='font-size: 70px;'>Virtual Chemistry Lab</h1>", unsafe_allow_html=True)
    st.subheader("Experiment with Reactants and Discover New Products!")
    st.write("Select two reactants from the menus below and click React to see what product is formed.")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.reactant1 = st.selectbox(
            "Select Reactant 1",
            options=reactant_options,
            key="sb_reactant1",
            index=reactant_options.index(st.session_state.reactant1)
        )
    with col2:
        st.session_state.reactant2 = st.selectbox(
            "Select Reactant 2",
            options=reactant_options,
            key="sb_reactant2",
            index=reactant_options.index(st.session_state.reactant2)
        )

    st.write("")  # Spacer

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        react_button = st.button("💥 React", use_container_width=True)
    with btn_col2:
        reset_button = st.button("🔄 Reset", use_container_width=True)

    # --- Reaction Logic ---
    if react_button:
        st.session_state.show_placeholder = False # Hide placeholder on react attempt
        st.session_state.error_message = None # Clear previous errors
        st.session_state.product_info = None # Clear previous results
        r1 = st.session_state.reactant1
        r2 = st.session_state.reactant2

        if r1 == "---Select---" or r2 == "---Select---":
            st.session_state.error_message = "⚠️ Please select two reactants."
        elif r1 == r2:
            st.session_state.error_message = "⚠️ Please select two different reactants."
        else:
            key1 = (r1, r2)
            key2 = (r2, r1)
            if key1 in reaction_data:
                st.session_state.product_info = reaction_data[key1]
            elif key2 in reaction_data:
                st.session_state.product_info = reaction_data[key2]
            else:
                st.session_state.error_message = "ℹ️ No reaction defined for this combination."

    if reset_button:
        st.session_state.reactant1 = reactant_options[0]
        st.session_state.reactant2 = reactant_options[0]
        st.session_state.product_info = None
        st.session_state.error_message = None
        st.session_state.show_placeholder = True # Show placeholder again
        st.rerun() # Rerun to clear selections visually and show placeholder

    # --- Display Error Messages ---
    if st.session_state.error_message:
        if "⚠️" in st.session_state.error_message:
             st.warning(st.session_state.error_message)
        else:
             st.info(st.session_state.error_message)


    # --- Display Product (in two columns) / Placeholder ---
    st.write("---") # Separator line

    if st.session_state.product_info:
        res_col1, res_col2 = st.columns(2) # Create columns for results

        with res_col1: # Column 1: Details
            st.title("Reaction Details")
            st.markdown(f"""
                    <ul style="font-size: 20px;">  
                        <li><strong>Product:</strong> {st.session_state.product_info.get("product", "N/A")}</li>
                        <li><strong>State:</strong> {st.session_state.product_info.get("state", "N/A")}</li>
                        <li><strong>Color:</strong> {st.session_state.product_info.get("color", "N/A")}</li>
                        <li><strong>Reaction Type:</strong> {st.session_state.product_info.get("reaction_type", "N/A")}</li>
                    </ul>
                    """, unsafe_allow_html=True)  # IMPORTANT: Allow HTML rendering

        with res_col2: # Column 2: Image
            image_url = st.session_state.product_info.get("image")
            if image_url:
                # Changed use_column_width=True to width=500
                st.image(image_url, caption="Reaction Result", width=300)
            else:
                st.write("*(No image available for this reaction)*") # Placeholder if no image URL

    elif st.session_state.show_placeholder: # Show placeholder only if flag is true
        st.markdown(
            """
            <div style="text-align: center; margin-top: 50px;">
            <h4>🔬 Virtual Chemistry Lab Output</h4>
            <p>Select reactants and press 'React' to see the results here!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- [Existing code for other pages (Periodic Table, etc.) remains the same] ---


elif key == 'Periodic Table':
    st.title("Periodic Table Explorer")
    df = pd.read_csv("periodic_table.csv")
    st.image("Periodictable.png")
    st.dataframe(df)
    choice = st.selectbox("Select element:", df["Symbol"] + " - " + df["Element"])
    sym = choice.split(" - ")[0]
    info = df[df["Symbol"]==sym].iloc[0]
    st.markdown(f"**Atomic Number:** {info.AtomicNumber}")
    st.markdown(f"**Atomic Mass:** {info.AtomicMass}")
    st.markdown(f"**Group:** {info.Group}, **Period:** {info.Period}")
    facts = {"H":"Most abundant.","He":"Used in balloons."}
    st.markdown(f"**Fun Fact:** {facts.get(sym, 'Add your fun fact!')}")

elif key == 'Periodic Trends':
    st.title("Periodic Trends")
    df = pd.read_csv("data/periodic_table.csv")
    trend = st

