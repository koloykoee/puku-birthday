import streamlit as st
import time

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Puku's Birthday Adventure ❤️",
    page_icon="🎂",
    layout="centered"
)

# ==========================================
# SESSION STATE
# ==========================================

if "step" not in st.session_state:
    st.session_state.step = 1

if "answer_checked" not in st.session_state:
    st.session_state.answer_checked = False

# ==========================================
# BEAUTIFUL DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #dff4ff,
        #c5e7ff,
        #a8dcff,
        #d8efff
    );
}

.block-container {
    max-width: 750px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

h1 {
    color: #145da0 !important;
    text-align: center;
    font-size: 38px !important;
}

h2, h3 {
    color: #145da0 !important;
    text-align: center;
}

p {
    color: #174873;
    text-align: center;
    font-size: 18px;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #ff69a6,
        #ff91bd
    );
    color: white;
    border: none;
    border-radius: 30px;
    height: 55px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #ff4081;
    color: white;
    transform: scale(1.03);
}

.stRadio label {
    color: #174873 !important;
    font-weight: bold;
}

hr {
    border-top: 2px dashed #ffffff;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# COMMON FUNCTIONS
# ==========================================

def next_page():
    st.session_state.step += 1
    st.rerun()


def heading(text):
    st.markdown(f"# {text}")
    st.markdown("---")


st.progress(st.session_state.step / 9)


# ==========================================
# PAGE 1 - SECRET GIFT
# ==========================================

if st.session_state.step == 1:

    st.balloons()

    st.title("🎁 A Secret Gift For Puku 🎁")

    st.markdown("""
    ### Hello Pukuuu! ❤️

    Tomar Lokkhi tomar jonno kichu ekta baniyeche...

    Jani oto bhalo hoyni, karon amar kache VFX nei
    ar somoy-o khub kom chilo.

    Tobuo nijer moto kore eituku banalam. 🥺

    Eta tomar jonno ekta chhoto
    virtual birthday adventure! 🥹💖

    **Ready to begin?**
    """)

    st.write("✨ Something special is waiting for you ✨")

    if st.button("💌 OPEN YOUR GIFT"):
        next_page()


# ==========================================
# PAGE 2 - OUR LITTLE MEMORIES
# ==========================================

elif st.session_state.step == 2:

    heading("📸 OUR LITTLE MEMORIES")

    st.markdown("""
    ### Every picture has a little story... ❤️

    Kichu moments special hoye thake,
    jegulo kokhono bhola jay na. 🥹
    """)

    # YOUR SPECIAL PHOTO

    st.image(
        r"C:\Users\Archita Dutta\Downloads\I love u.jpeg",
        caption="A little memory to remember ❤️",
        use_container_width=True
    )

    st.markdown("""
    ### Distance doesn't erase memories. ❤️
    """)

    if st.button("💌 UNLOCK NEXT SURPRISE"):
        next_page()


# ==========================================
# PAGE 3 - CHOCOLATE COLLECTION
# ==========================================

elif st.session_state.step == 3:

    heading("🍫 CHOCOLATE COLLECTION")

    st.markdown("""
    ### Congratulations Pukuuu! 🥳

    You have unlocked your chocolate box!

    🍫 🍫 🍫

    🍫 🍫 🍫

    Total Chocolates: 6

    Special Note:

    Sob chocolate tomar jonno...

    Kintu unfortunately egulo virtual! 🤣
    """)

    if st.button("🎮 CONTINUE ADVENTURE"):
        next_page()


# ==========================================
# PAGE 4 - PUKU EXAM
# ==========================================

elif st.session_state.step == 4:

    heading("😂 OFFICIAL PUKU EXAM")

    st.markdown("""
    ### Attention Puku! 🚨

    You have one important question.

    Answer carefully!
    """)

    answer = st.radio(
        "Lokkhi-r favourite person ke?",
        [
            "Pizza 🍕",
            "Sleeping 😴",
            "Puku ❤️",
            "Chocolate 🍫"
        ],
        index=None
    )

    if st.button("SUBMIT ANSWER"):

        if answer == "Puku ❤️":

            st.success("""
            🎉 CORRECT ANSWER!

            Congratulations Puku!

            You passed the exam with full marks! ❤️
            """)

            st.session_state.answer_checked = True

        elif answer is None:

            st.warning("Age answer select koro! 😂")

        else:

            st.error("""
            WRONG ANSWER! 🤣

            Ektu bhalo kore abar bhabo!
            """)

    if st.session_state.answer_checked:

        if st.button("🏆 CLAIM YOUR REWARD"):
            st.session_state.answer_checked = False
            next_page()


# ==========================================
# PAGE 5 - AWARD CEREMONY
# ==========================================

elif st.session_state.step == 5:

    st.balloons()

    heading("🏆 THE AWARD CEREMONY")

    st.markdown("""
    ## 🥇 WINNER 🥇

    # ❤️ PUKU ❤️

    Congratulations!

    You have officially won:

    🏆 Favourite Human Award

    🧸 Best Teddy Collector

    🍫 Chocolate Champion

    😂 Professional Lokkhi Irritator

    💖 Lifetime Special Person Award

    **Sponsored by:**

    LOKKHI 🌸
    """)

    if st.button("💌 OPEN A SPECIAL LETTER"):
        next_page()


# ==========================================
# PAGE 6 - SPECIAL LETTER
# ==========================================

elif st.session_state.step == 6:

    heading("💌 A LETTER FOR PUKU")

    st.markdown("""
    ### Dear Puku ❤️

    Jani tomai kichui dite parini
    cheshta krechi sudhu kichu korar🥺.

    Eta perfect kina jani na...

    Distance thakleo kichu moments
    khub special hoye thake.

    Tomar Hashi, tomar ultapalta mukher ongovongi,
    ar amader chhoto chhoto memories...

    Sobkichu amar kache special.

    I hope tomar birthday-ta
    onek sundor katuk.

    Always keep smiling! 🥹💖
    I wish jodi ami thakte partam.

    **With lots of wishes,**

    Your Lokkhi 🌸
    """)

    if st.button("📜 UNLOCK THE SECRET RULES"):
        next_page()


# ==========================================
# PAGE 7 - RELATIONSHIP RULES
# ==========================================

elif st.session_state.step == 7:

    heading("📜 OFFICIAL PUKU RULEBOOK")

    st.markdown("""
    ### Important Instructions 😂

    **RULE 01**

    Lokkhi-r kotha mon diye shunte hobe. 😌

    **RULE 02**

    Puku-r cute behaviour compulsory. ❤️

    **RULE 03**

    Birthday boy-er kono kaj nei...

    Sudhu enjoy korte hobe! 🎂

    **RULE 04**

    R Amk onk onk valobashte hbe

    **RULE 05**

    Sobsomoi tomar hashi mukh ta jeno dekhte paii..

    **RULE 06**

    Ei website-er creator-ke
    ekta thank you bolte hobe! 🤣
    """)

    if st.button("🎵 UNLOCK OUR SPECIAL SONG"):
        next_page()


# ==========================================
# PAGE 8 - SPECIAL SONG
# ==========================================

elif st.session_state.step == 8:

    heading("🎵 A SPECIAL SONG FOR YOU")

    st.markdown("""
    ### Some songs hold special memories... 🥹

    Ei gaan-ta shunle
    amar kotha mone porbe. ❤️

    Sometimes music says
    what words cannot express.
    """)

    st.link_button(
        "🎵 PLAY OUR SPECIAL SONG ❤️",
        "https://youtu.be/tfOhP4Anuq0?si=A1sv-8IKHzwRge6E"
    )

    st.write("🎧 Listen and enjoy!")

    if st.button("🎂 OPEN THE FINAL SURPRISE"):
        next_page()


# ==========================================
# PAGE 9 - FINAL BIRTHDAY
# ==========================================

elif st.session_state.step == 9:

    st.balloons()

    st.snow()

    st.title("🎂 HAPPY BIRTHDAY PUKU! 🎂")

    st.markdown("""
    # 🎉🥳🎈

    ## MISSION COMPLETED!

    ✅ Teddy Collected

    ✅ Chocolates Unlocked

    ✅ Puku Exam Passed

    ✅ Favourite Human Award Won

    ✅ Special Letter Received

    ✅ Secret Song Unlocked

    """)

    st.markdown("---")

    st.markdown("""
    ## 🥹💖 A LITTLE MESSAGE FOR YOU

    Mr. theke Puku howa manushta...

    Amar khub priyo. ❤️

    Dure thakleo protidin
    tomar kotha mone pore.

    Ami hoyto sobsomoy
    tomar pashe thakte pari na.

    Kintu tomake valobasha
    kokhono kombe na.

    Tomake niye haste bhalo lage.

    Tomake niye rag korte bhalo lage.

    Tomake niye shopno dekhte bhalo lage.

    I wish you happiness,
    success and endless beautiful moments.

    May this new year of your life
    bring you everything you deserve.

    ### HAPPY BIRTHDAY, PUKU! 🎂

    ### INFINITY LOVE ACTIVATED ♾️❤️

    -- TOMAR LOKKHI 🌸
    """)

    st.balloons()

    st.markdown("---")

    st.success("🎁 You have completed Puku's Birthday Adventure!")

    if st.button("🔄 REPLAY THE SURPRISE"):

        st.session_state.step = 1
        st.session_state.answer_checked = False
        st.rerun()
