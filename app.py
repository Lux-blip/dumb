import streamlit as st
import random
import time

st.set_page_config(page_title="DUMB STUFF", page_icon="🗑️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Courier Prime', monospace;
}
.big-title {
    font-size: 72px;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -2px;
    margin-bottom: 8px;
}
.subtitle {
    color: #888;
    font-size: 13px;
    margin-bottom: 40px;
}
.section-num {
    color: #bbb;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.section-title {
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #444;
    margin-bottom: 12px;
}
.card {
    padding: 24px;
    border-radius: 6px;
    border: 2px solid #1a1a1a;
    margin-bottom: 8px;
}
.result-text {
    font-size: 16px;
    line-height: 1.7;
    min-height: 50px;
}
.tag {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 3px;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: white;
    margin-bottom: 8px;
}
hr { border-top: 2px solid #1a1a1a; }
</style>
""", unsafe_allow_html=True)

# ============ DATA ============

FACTS = [
    "A group of flamingos is called a 'flamboyance'. Obviously.",
    "Crows hold grudges. They will remember your face and judge you forever.",
    "Cleopatra lived closer in time to the Moon landing than to the pyramids being built.",
    "The word 'nerd' was first used in a Dr. Seuss book.",
    "Bananas are technically berries. Strawberries are not.",
    "A day on Venus is longer than a year on Venus.",
    "Wombat poop is cube-shaped. Nature said: why not.",
    "Humans share 60% of their DNA with bananas. Make of that what you will.",
    "The inventor of the frisbee was turned into a frisbee after he died.",
    "Snails can sleep for 3 years. Goals.",
    "There are more possible games of chess than atoms in the observable universe.",
    "A shrimp's heart is in its head.",
    "Otters hold hands while sleeping so they don't drift apart.",
    "The blob of toothpaste on your brush is called a 'nurdle'.",
    "Butterflies taste with their feet.",
]

COMPLIMENTS = [
    "You look incredibly average today. Refreshing.",
    "Your energy is giving 'main character who is also kind of annoying'.",
    "You probably smell fine.",
    "Statistically, you are better than at least one person.",
    "Your vibe? Detectable.",
    "You're doing a great job existing.",
    "Honestly? Could be worse.",
    "You have a face and everything.",
    "Your presence in this room is noted.",
    "You seem like someone who has tried.",
]

EXCUSES = [
    "I can't come in today. My horoscope said 'rest'.",
    "Sorry I'm late. I was doing nothing and lost track of time.",
    "I didn't do my homework because I was emotionally unavailable.",
    "Can't make it to the meeting. My cat looked at me weird and now I need to process.",
    "I forgot because Mercury is in retrograde and also I didn't care.",
    "I was going to reply but then I didn't.",
    "My WiFi was too slow to feel motivated.",
    "I had a scheduling conflict with my nap.",
    "I lost track of time staring at a wall. Productive wall though.",
    "My hands weren't in the mood.",
]

ROASTS = [
    "You have the energy of a half-charged phone.",
    "You're the human equivalent of a participation trophy.",
    "Your vibe is 'forgot to reply for 3 weeks'.",
    "You remind me of a printer that says it's online but refuses to print.",
    "You're like a free trial of a person.",
    "You have the decision-making skills of a Roomba near stairs.",
    "Your aura is beige. Comfortably, committedly beige.",
    "You're the type to clap when the plane lands.",
    "Your superpower is being simultaneously everywhere and nowhere.",
    "You're a background character in your own life.",
]

LIFE_ADVICE = [
    "Drink water. Or don't. You'll probably be fine either way.",
    "The real treasure was the snacks we ate along the way.",
    "If you're unsure whether to send that text, don't.",
    "Nobody is thinking about you as much as you think. That's actually great news.",
    "Sleep is free. Use it.",
    "You don't have to have it figured out. Nobody does. It's chaos.",
    "Wear the thing. Do the thing. Go to bed.",
    "If the vibe is off, leave.",
    "You are allowed to just sit there sometimes.",
    "Eat a vegetable occasionally. Just one. For the bit.",
]

PREDICTIONS = [
    "Today you will open the fridge, find nothing new, and close it.",
    "Someone will say 'per my last email' at you this week.",
    "You will start a new hobby and abandon it within 9 days.",
    "A song will get stuck in your head at 2am. It will be a jingle.",
    "You will almost text your ex. You won't. Good.",
    "A pigeon will judge you. You'll feel it.",
    "You will have an excellent thought in the shower and forget it immediately.",
    "Something will buffer at the worst possible moment.",
    "You will say 'sounds good' when you're not sure what was said.",
    "A nap will fix everything. Or at least postpone it.",
]

WOULD_YOU_RATHER = [
    ["Fight one horse-sized duck", "Fight 100 duck-sized horses"],
    ["Only speak in rhymes for a year", "Only walk sideways for a year"],
    ["Know how you'll die but not when", "Know when but not how"],
    ["Never use social media again", "Never watch movies or TV again"],
    ["Have unlimited money but no friends", "Have unlimited friends but no money"],
    ["Be always 10 minutes late", "Always 20 minutes early"],
    ["Lose your keys weekly", "Lose your phone weekly"],
    ["Only eat hot food cold", "Only eat cold food hot"],
]

CONSPIRACIES = [
    "Elevators have a 'close door' button that does literally nothing.",
    "Cereal companies invented breakfast so you'd buy cereal.",
    "The 'new car smell' is just chemicals and we decided it was luxury.",
    "Parking lots are designed to make you give up and go home.",
    "Alarm clock snooze buttons were invented to make you late.",
    "Office 'reply-all' was a bug they kept in on purpose.",
    "'You may have already won' means you haven't won.",
    "The backspace key is doing most of the work and getting none of the credit.",
]

HAIKUS = [
    ["Empty fridge at night", "Stare into its cold bright void", "Close it. Open. Close."],
    ["Meeting could've been", "An email. It wasn't though.", "Here we are again."],
    ["Phone at 3% —", "A slow descent into fear.", "Charger nowhere near."],
    ["Autocorrect changed", "Your words into something cursed.", "You sent it. It's done."],
    ["Scroll. Scroll. Scroll. Scroll. Scroll.", "Nothing new but you keep on.", "Scroll. Scroll. Scroll. Scroll. Sleep."],
]

VIBE_CHECKS = [
    ("🌵", "Dry", "You are weathering something. Quietly. Correctly."),
    ("🌧️", "Drizzly", "Not bad. Not great. Adequately moist."),
    ("☀️", "Sunny", "Suspiciously good energy. What happened?"),
    ("🌪️", "Chaotic", "A lot is happening. None of it is planned."),
    ("🌫️", "Foggy", "Unclear. Drifting. Vaguely cozy about it."),
    ("⛈️", "Stormy", "You are going through something. The drama is real."),
    ("🌈", "Post-storm", "Things were bad. They're better now. You survived."),
    ("❄️", "Frozen", "You have entered stasis. Nothing moves."),
]

NPC_LINES = [
    "I used to be an adventurer like you. Then I got a mortgage.",
    "Have you tried turning it off and on again?",
    "Rumor has it, the coffee machine is haunted.",
    "I can't leave this spot. I've been here since Tuesday.",
    "The quest? Oh, I gave up on the quest.",
    "My inventory is full. Of regrets.",
    "Greetings, traveler. Do you have the Wi-Fi password?",
    "I am but a simple villager who has read all of Twitter.",
]

TRUTH_OR_DARE = [
    ("truth", "What's the most embarrassing thing you've Googled?"),
    ("truth", "What's an opinion you hold that you'd never say out loud?"),
    ("truth", "Name a food you pretend to like for social reasons."),
    ("dare", "Text someone 'this isn't what it looks like' with no context."),
    ("dare", "Set your status to 'in a meeting' and leave it for 48 hours."),
    ("dare", "Reply to the next email you get with just 'noted'."),
    ("truth", "What's the latest you've stayed up doing something dumb?"),
    ("dare", "Change your phone wallpaper to a picture of a random vegetable."),
]

PERSONALITY_TRAITS = [
    "Chaotic energy",
    "Repressed feelings",
    "Snack dependency",
    "Main character syndrome",
    "Overthinking",
    "Functional chaos",
]

MOODS = [
    ("🚗💧", "crying in the car", "Phoebe Bridgers, boygenius, Mitski"),
    ("😈", "villain era", "Nine Inch Nails, HEALTH, Fever Ray"),
    ("🎬", "main character montage", "Hozier, Florence + Machine, The National"),
    ("🌀", "chaotic good", "100 gecs, Charli XCX, Yves Tumor"),
    ("☕", "cozy doing nothing", "Norah Jones, Air, Beach House"),
    ("🌌", "existential 3am", "Grouper, Daughter, Bon Iver"),
    ("✨", "revenge glow-up", "Carly Rae Jepsen, Kim Petras, Robyn"),
]

HOTLINE_RESPONSES = [
    "Option A will definitely haunt you. Go with B.",
    "Neither. Go to bed.",
    "Yes. Do it. What's the worst that could happen? (don't answer that)",
    "The fact that you're asking means you already know the answer.",
    "Statistically, this will make a great story in 5 years.",
    "No. Absolutely not. Why are you like this.",
    "You're going to do it anyway, so: fine. just fine.",
    "The hotline recommends a snack break and revisiting this tomorrow.",
]

WIKI_TOPICS = [
    "The history of competitive eating",
    "Medieval siege warfare toilets",
    "The taxonomy of imaginary animals",
    "Why hot dogs are sandwiches (legally)",
    "The economics of the rubber duck industry",
    "Competitive dog grooming controversies",
    "The philosophy of parking lots",
    "Why we yawn (nobody actually knows)",
    "The surprisingly complex history of the number zero",
    "Famous horses throughout history",
]

NOTHING_BUTTON_RESPONSES = [
    "nothing happened.",
    "still nothing.",
    "you clicked it again.",
    "wow.",
    "ok stop.",
    "seriously.",
    "fine.",
    "...",
    "ok i respect the commitment.",
    "FINE. here's a star: ⭐",
    "that's all you get.",
    "go touch grass.",
]

# ============ HEADER ============

st.markdown('<div class="big-title">DUMB<br>STUFF</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">20 features · zero purpose · you\'re welcome</div>', unsafe_allow_html=True)
st.markdown("---")

# ============ INIT SESSION STATE ============

defaults = {
    "fact_idx": 0,
    "nothing_clicks": 0,
    "wyr_idx": 0,
    "wyr_choice": None,
    "clicker_score": 0,
    "clicker_multiplier": 1,
    "clicker_upgrades": 0,
    "wiki_running": False,
    "wiki_topic": None,
    "wiki_start": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ============ FEATURE 1: USELESS FACTS ============

st.markdown('<div class="section-num">01</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Useless Facts</div>', unsafe_allow_html=True)
with st.container():
    st.info(f"**FACT:** {FACTS[st.session_state.fact_idx]}")
    if st.button("Give me another →", key="fact_btn"):
        st.session_state.fact_idx = (st.session_state.fact_idx + 1) % len(FACTS)
        st.rerun()
st.markdown("---")

# ============ FEATURE 2: COMPLIMENTS ============

st.markdown('<div class="section-num">02</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Unsolicited Compliments</div>', unsafe_allow_html=True)
if st.button("Compliment me 🙏", key="compliment_btn"):
    st.success(f"**YOU:** {random.choice(COMPLIMENTS)}")
st.markdown("---")

# ============ FEATURE 3: EXCUSE GENERATOR ============

st.markdown('<div class="section-num">03</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Excuse Generator</div>', unsafe_allow_html=True)
if "current_excuse" not in st.session_state:
    st.session_state.current_excuse = None
if st.button("Generate Excuse", key="excuse_btn"):
    st.session_state.current_excuse = random.choice(EXCUSES)
if st.session_state.current_excuse:
    st.warning(f"**EXCUSE:** {st.session_state.current_excuse}")
    st.code(st.session_state.current_excuse, language=None)
    st.caption("☝️ click the copy icon on the right")
st.markdown("---")

# ============ FEATURE 4: BUTTON THAT DOES NOTHING ============

st.markdown('<div class="section-num">04</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Button That Does Nothing</div>', unsafe_allow_html=True)
st.caption("this button does absolutely nothing")
if st.button("DO NOT PRESS", key="nothing_btn"):
    st.session_state.nothing_clicks += 1
if st.session_state.nothing_clicks > 0:
    n = st.session_state.nothing_clicks
    msg = NOTHING_BUTTON_RESPONSES[min(n - 1, len(NOTHING_BUTTON_RESPONSES) - 1)]
    suffix = f" (×{n})" if n > 9 else ""
    st.error(f"{msg}{suffix}")
st.markdown("---")

# ============ FEATURE 5: ROAST GENERATOR ============

st.markdown('<div class="section-num">05</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Roast Generator</div>', unsafe_allow_html=True)
if st.button("🔥 Roast Me", key="roast_btn"):
    st.error(f"🔥 {random.choice(ROASTS)}")
st.markdown("---")

# ============ FEATURE 6: LIFE ADVICE ============

st.markdown('<div class="section-num">06</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Life Advice Dispenser</div>', unsafe_allow_html=True)
st.caption("shake the magic 8-ball of mediocre wisdom")
if st.button("🔮 Dispense Wisdom", key="advice_btn"):
    with st.spinner("shaking..."):
        time.sleep(0.4)
    st.info(f"🔮 {random.choice(LIFE_ADVICE)}")
st.markdown("---")

# ============ FEATURE 7: PSYCHIC PREDICTIONS ============

st.markdown('<div class="section-num">07</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Psychic Predictions</div>', unsafe_allow_html=True)
st.caption("the oracle sees all. all is mundane.")
if st.button("🔭 Predict My Future", key="predict_btn"):
    with st.spinner("consulting the vibes..."):
        time.sleep(0.6)
    st.info(f"🔭 {random.choice(PREDICTIONS)}")
st.markdown("---")

# ============ FEATURE 8: WOULD YOU RATHER ============

st.markdown('<div class="section-num">08</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Would You Rather</div>', unsafe_allow_html=True)
st.caption("no wrong answer (there is a wrong answer)")
pair = WOULD_YOU_RATHER[st.session_state.wyr_idx]
col1, col2 = st.columns(2)
with col1:
    if st.button(f"A: {pair[0]}", key="wyr_a"):
        st.session_state.wyr_choice = 0
with col2:
    if st.button(f"B: {pair[1]}", key="wyr_b"):
        st.session_state.wyr_choice = 1
if st.session_state.wyr_choice is not None:
    chosen = pair[st.session_state.wyr_choice]
    st.success(f"You chose: **{chosen}**. Fascinating.")
    if st.button("Next Dilemma →", key="wyr_next"):
        st.session_state.wyr_idx = (st.session_state.wyr_idx + 1) % len(WOULD_YOU_RATHER)
        st.session_state.wyr_choice = None
        st.rerun()
st.markdown("---")

# ============ FEATURE 9: CONSPIRACY CORNER ============

st.markdown('<div class="section-num">09</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Conspiracy Corner</div>', unsafe_allow_html=True)
st.caption("100% true, probably")
if st.button("🤫 Expose The Truth", key="conspiracy_btn"):
    st.session_state.current_conspiracy = random.choice(CONSPIRACIES)
if "current_conspiracy" in st.session_state:
    st.warning(f"🤫 {st.session_state.current_conspiracy}")
st.markdown("---")

# ============ FEATURE 10: HAIKU ============

st.markdown('<div class="section-num">10</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Haiku of the Moment</div>', unsafe_allow_html=True)
st.caption("5-7-5 syllables of truth")
if st.button("Generate Haiku", key="haiku_btn"):
    haiku = random.choice(HAIKUS)
    st.markdown(f"""
> *{haiku[0]}*  
> *{haiku[1]}*  
> *{haiku[2]}*
""")
st.markdown("---")

# ============ FEATURE 11: VIBE CHECK ============

st.markdown('<div class="section-num">11</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Vibe Check</div>', unsafe_allow_html=True)
st.caption("scientifically certified results")
if st.button("Check My Vibe", key="vibe_btn"):
    with st.spinner("scanning..."):
        time.sleep(1)
    emoji, label, desc = random.choice(VIBE_CHECKS)
    st.markdown(f"### {emoji} {label}")
    st.info(desc)
st.markdown("---")

# ============ FEATURE 12: NPC ENCOUNTER ============

st.markdown('<div class="section-num">12</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">NPC Encounter</div>', unsafe_allow_html=True)
st.caption("press A to interact")
if st.button("▶ Press A", key="npc_btn"):
    line = random.choice(NPC_LINES)
    st.code(f"VILLAGER: {line}", language=None)
st.markdown("---")

# ============ FEATURE 13: TRUTH OR DARE ============

st.markdown('<div class="section-num">13</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Truth or Dare</div>', unsafe_allow_html=True)
st.caption("internet edition")
col1, col2 = st.columns(2)
with col1:
    truth_btn = st.button("Truth", key="truth_btn")
with col2:
    dare_btn = st.button("Dare", key="dare_btn")
if truth_btn:
    truths = [(t, q) for t, q in TRUTH_OR_DARE if t == "truth"]
    _, question = random.choice(truths)
    st.error(f"**TRUTH:** {question}")
if dare_btn:
    dares = [(t, q) for t, q in TRUTH_OR_DARE if t == "dare"]
    _, question = random.choice(dares)
    st.warning(f"**DARE:** {question}")
st.markdown("---")

# ============ FEATURE 14: FAKE PERSONALITY ============

st.markdown('<div class="section-num">14</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Personality Breakdown</div>', unsafe_allow_html=True)
st.caption("based on nothing")
if st.button("Analyze Me", key="personality_btn"):
    with st.spinner("analyzing your entire being..."):
        time.sleep(1.5)
    for trait in PERSONALITY_TRAITS:
        val = random.randint(10, 99)
        st.text(trait)
        st.progress(val / 100)
        st.caption(f"{val}%")
st.markdown("---")

# ============ FEATURE 15: MOOD PLAYLIST ============

st.markdown('<div class="section-num">15</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Mood → Playlist</div>', unsafe_allow_html=True)
st.caption("vibes only, no links, you figure it out")
mood_emojis = [m[0] for m in MOODS]
mood_labels = [m[1] for m in MOODS]
selected_mood = st.radio("pick your mood:", [f"{e} {l}" for e, l in zip(mood_emojis, mood_labels)], key="mood_radio", label_visibility="collapsed")
if selected_mood:
    idx = [f"{e} {l}" for e, l in zip(mood_emojis, mood_labels)].index(selected_mood)
    _, _, artists = MOODS[idx]
    st.success(f"**Listen to:** {artists}")
st.markdown("---")

# ============ FEATURE 16: COUNTDOWN TO NOTHING ============

st.markdown('<div class="section-num">16</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Countdown to Nothing</div>', unsafe_allow_html=True)
st.caption("meaningless events, precisely timed")
events = {
    "end of this sentence": 5,
    "next awkward silence": 12,
    "you forgetting this website exists": 30,
    "an email you'll ignore": 60,
}
chosen_event = st.selectbox("countdown to:", list(events.keys()), key="countdown_select")
if st.button("Start Countdown", key="countdown_btn"):
    secs = events[chosen_event]
    bar = st.progress(0)
    status = st.empty()
    for i in range(secs, 0, -1):
        status.markdown(f"### {i}s until *{chosen_event}*")
        bar.progress((secs - i) / secs)
        time.sleep(1)
    bar.progress(1.0)
    status.success(f"✓ it happened. nothing changed.")
st.markdown("---")

# ============ FEATURE 17: BAD DECISION HOTLINE ============

st.markdown('<div class="section-num">17</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Bad Decision Hotline</div>', unsafe_allow_html=True)
st.caption("staffed by nobody qualified")
if st.button("📞 Call The Hotline", key="hotline_btn"):
    with st.spinner("📞 ringing... hold music: gentle bossa nova"):
        time.sleep(1.8)
    st.info(f"**HOTLINE:** {random.choice(HOTLINE_RESPONSES)}")
st.markdown("---")

# ============ FEATURE 18: CLICKER GAME ============

st.markdown('<div class="section-num">18</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Clicker Game</div>', unsafe_allow_html=True)
st.caption("the whole genre reduced to 1 section")
st.metric("Score", st.session_state.clicker_score, delta=f"×{st.session_state.clicker_multiplier} per click")
upgrade_cost = (st.session_state.clicker_upgrades + 1) * 50
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👆 CLICK", key="clicker_btn"):
        st.session_state.clicker_score += st.session_state.clicker_multiplier
        st.rerun()
with col2:
    upgrade_label = f"Upgrade (costs {upgrade_cost})"
    if st.button(upgrade_label, key="upgrade_btn", disabled=st.session_state.clicker_score < upgrade_cost):
        st.session_state.clicker_score -= upgrade_cost
        st.session_state.clicker_multiplier += 1
        st.session_state.clicker_upgrades += 1
        st.rerun()
with col3:
    if st.button("Reset", key="clicker_reset"):
        st.session_state.clicker_score = 0
        st.session_state.clicker_multiplier = 1
        st.session_state.clicker_upgrades = 0
        st.rerun()
if st.session_state.clicker_score > 500:
    st.success("ok you're actually playing this. respect.")
if st.session_state.clicker_score > 2000:
    st.warning("you need to go outside.")
st.markdown("---")

# ============ FEATURE 19: SOUNDBOARD ============

st.markdown('<div class="section-num">19</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Soundboard (No Sound)</div>', unsafe_allow_html=True)
st.caption("your device does the sound (it doesn't)")
sounds = ["🎺", "🥁", "🎸", "🎹", "🎻", "📯"]
cols = st.columns(len(sounds))
for i, (col, sound) in enumerate(zip(cols, sounds)):
    with col:
        if st.button(sound, key=f"sound_{i}"):
            st.caption(f"you pressed {sound}. the music is in your heart.")
st.markdown("---")

# ============ FEATURE 20: WIKIPEDIA RABBIT HOLE ============

st.markdown('<div class="section-num">20</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Wikipedia Rabbit Hole Simulator</div>', unsafe_allow_html=True)
st.caption("escape is optional")
if st.button("Enter The Hole 🕳️", key="wiki_start_btn"):
    st.session_state.wiki_topic = random.choice(WIKI_TOPICS)
    st.session_state.wiki_start = time.time()
    st.session_state.wiki_running = True
    st.rerun()
if st.session_state.wiki_running and st.session_state.wiki_topic:
    elapsed = int(time.time() - st.session_state.wiki_start)
    st.markdown(f"**START ARTICLE:** `{st.session_state.wiki_topic}`")
    st.markdown(f"### ⏱️ {elapsed}s in the hole")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💪 I Escaped", key="wiki_escaped"):
            st.session_state.wiki_running = False
            st.success(f"Escaped in {elapsed}s. Impressive self control.")
    with col2:
        if st.button("🕳️ I Fell In", key="wiki_fell"):
            st.session_state.wiki_running = False
            st.error(f"You fell in at {elapsed} seconds. Respectable.")
    st.button("🔄 Refresh Timer", key="wiki_refresh")

# ============ FOOTER ============

st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-family: monospace; font-size:11px; color:#bbb; letter-spacing:2px;'>"
    "© DUMB STUFF · 20 FEATURES · ALL RIGHTS RESERVED · NONE OF THIS MATTERS"
    "</div>",
    unsafe_allow_html=True
)
