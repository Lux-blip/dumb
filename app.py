import streamlit as st
import random
import time
import datetime

st.set_page_config(page_title="DUMB STUFF", page_icon="🗑️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap');
html, body, [class*="css"] { font-family: 'Courier Prime', monospace; }
.big-title { font-size: 72px; font-weight: 900; line-height: 1; letter-spacing: -2px; margin-bottom: 8px; }
.subtitle { color: #888; font-size: 13px; margin-bottom: 40px; }
hr { border-top: 2px solid #1a1a1a; }
</style>
""", unsafe_allow_html=True)

# ============ ALL DATA ============

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
    "Chaotic energy", "Repressed feelings", "Snack dependency",
    "Main character syndrome", "Overthinking", "Functional chaos",
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
    "nothing happened.", "still nothing.", "you clicked it again.",
    "wow.", "ok stop.", "seriously.", "fine.", "...",
    "ok i respect the commitment.", "FINE. here's a star: ⭐",
    "that's all you get.", "go touch grass.",
]

APOLOGIES = [
    "I'm sorry you feel that way. (Not sorry about what I did.)",
    "My deepest apologies for the inconvenience of my existence.",
    "I regret that this happened to you, specifically.",
    "Sorry! But also, have you considered that you might be wrong?",
    "On behalf of myself, I apologize. On behalf of the situation, no.",
    "I'm sorry. But in my defense, I was tired.",
    "Truly, deeply, comprehensively sorry. (Terms apply.)",
    "Apologies for any confusion caused by me being correct.",
]

JOB_TITLES = [
    "Chief Vibes Officer", "Senior Nap Consultant", "Director of Unfinished Projects",
    "Head of Sending Memes", "Principal Snack Strategist", "VP of Doing The Most",
    "Associate Overthinker", "Global Head of Ghosting", "Lead Chaos Engineer",
    "Junior Everything, Senior Nothing", "Executive Producer of Excuses",
    "Chief Emotional Support Animal", "Director of Aggressive Mediocrity",
]

RED_FLAGS = [
    "Says 'I'm not like other people' while being exactly like other people.",
    "Has 47 unread texts but posts Instagram stories.",
    "Their Spotify is 90% one artist from 2016.",
    "Calls movies 'films' but only watched it on a phone.",
    "Describes themselves as 'brutally honest' but mostly just brutal.",
    "Still uses 'per my last email' unironically.",
    "Their personality is their job.",
    "Says 'no offense' before being extremely offensive.",
    "Claps at the end of movies in an empty room at home.",
    "Puts their Myers-Briggs type in their bio.",
]

GREEN_FLAGS = [
    "Laughs at their own jokes before the punchline.",
    "Has a dedicated snack drawer and will share.",
    "Texts back within a reasonable amount of time.",
    "Says 'I don't know' when they don't know.",
    "Has strong opinions about sandwiches.",
    "Remembers small things you said months ago.",
    "Genuinely excited about other people's good news.",
    "Can sit in silence without making it weird.",
    "Their houseplants are mostly alive.",
    "Uses turn signals. Every time.",
]

SHOWER_THOUGHTS = [
    "If you clean your vacuum, you're the vacuum cleaner.",
    "The word 'bed' looks like a bed.",
    "You've never seen your own face in real time. Only reflections and recordings.",
    "Every time you learn something new, something else is slightly pushed out.",
    "Technically, you're always in the center of your own universe.",
    "At some point, someone had to invent the word 'invention'.",
    "Your future self will look back on right now as 'the old days'.",
    "Nothing is on fire until it is, and then it's too late to be surprised.",
    "The oldest photo of you exists without your knowledge or consent.",
    "You've never actually seen the back of your own head without help.",
]

STAR_SIGNS_DUMB = {
    "♈ Aries": "Aggressively online. Has opinions about everything. Sends voice memos.",
    "♉ Taurus": "Refuses to move. Comfortable. Will not be rushed. Snack present.",
    "♊ Gemini": "Two moods: fine and absolutely not fine. Switches mid-sentence.",
    "♋ Cancer": "Has saved every text since 2014. Cried about a commercial today.",
    "♌ Leo": "Sent themselves a compliment and screenshot it. For inspiration.",
    "♍ Virgo": "Made a to-do list to make their to-do list. It's color coded.",
    "♎ Libra": "Cannot choose a restaurant. Has been choosing for 45 minutes. Still going.",
    "♏ Scorpio": "Knows everything about you. Has said nothing. Waiting.",
    "♐ Sagittarius": "Booked a one-way flight at 2am. Cancelled it at 3am. Will retry.",
    "♑ Capricorn": "Already done. You're still on step one. They don't understand.",
    "♒ Aquarius": "Does not care what you think. Deeply cares what you think.",
    "♓ Pisces": "Living in a movie in their head. The movie is extremely dramatic.",
}

FAKE_AWARDS = [
    "🏆 Most Likely to Open Fridge 12 Times and Find Nothing",
    "🥇 Gold Medal: Overthinking a Simple Text",
    "🎖️ Distinguished Service Award for Staying in Bed",
    "🏅 Excellence in Saying 'I'll Do It Later'",
    "🌟 Star of the Year: Forgetting Why You Walked Into a Room",
    "🎗️ Ribbon of Honor: Ghosting a Reply You Definitely Saw",
    "🏆 Championship: Turning Off Lights in Empty Rooms Nobody Asked About",
    "🥈 Silver Medal: Almost Saying Something Then Not",
    "🎪 Lifetime Achievement: Surviving Unnecessary Drama",
    "🏆 Grand Prize: Being Fine, Actually",
]

CURSED_MENU_ITEMS = [
    "Lukewarm Soup of Ambiguity — served at whatever temperature",
    "Deconstructed Water — wet, but make it art",
    "Pan-Seared Nothing — with a reduction of silence",
    "The Manager Special — nobody ordered this",
    "Artisanal Bread of Regret — baked this morning, hard by noon",
    "Seasonal Existential Crisis — market price",
    "Foam of Uncertainty — pairs well with 'I don't know'",
    "The Tasting Menu — 14 courses you didn't want",
]

LOADING_SCREENS = [
    "Loading your entire personality...",
    "Generating reasons to stay in bed...",
    "Downloading more RAM...",
    "Consulting the void...",
    "Buffering your life choices...",
    "Compiling your unread notifications...",
    "Rendering your unfinished projects...",
    "Please wait while we locate your motivation...",
    "Syncing your crippling indecision...",
    "Almost done pretending to work...",
]

BAND_NAME_PARTS_A = [
    "Screaming", "Quiet", "Angry", "The Gentle", "Burning", "Sad", "Electric",
    "Haunted", "Dead", "Crying", "The Awkward", "Frozen", "Cosmic",
]
BAND_NAME_PARTS_B = [
    "Furniture", "Accountants", "Ghosts", "Teenagers", "Parking Lots",
    "Algorithms", "Sandwiches", "Dentists", "Pigeons", "Spreadsheets",
    "Landlords", "WiFi", "Receipts", "Playlists", "Notifications",
]

FORTUNE_COOKIES = [
    "A surprise awaits you. It is a bill.",
    "You will find what you are looking for. In the last place you look. Obviously.",
    "Someone is thinking of you. They are mildly annoyed.",
    "Great things come to those who wait. You have been waiting. Keep waiting.",
    "Your lucky numbers are: no.",
    "Happiness is just around the corner. The corner is far.",
    "Today is a good day to do nothing and call it 'recharging'.",
    "You will receive unexpected news. It will be about a subscription you forgot.",
    "Adventure awaits. The adventure is finding parking.",
    "Good fortune smiles upon you. It's more of a smirk.",
]

WRONG_ANSWERS = [
    ("What is 2+2?", "Fish."),
    ("What is the capital of France?", "A building."),
    ("How many days in a week?", "Enough."),
    ("What comes after winter?", "More winter, honestly."),
    ("What is water made of?", "Wet."),
    ("How far is the moon?", "Pretty far."),
    ("What is the speed of light?", "Fast."),
    ("What is a noun?", "A doing word. No wait."),
    ("What is the tallest mountain?", "A very big hill."),
    ("What is time?", "A flat circle. Or a cone. Science is unclear."),
]

ZODIAC_COMPATIBILITY = [
    ("🔥 Extremely Compatible", "You are both disasters. It works."),
    ("💀 Not Compatible", "Run. Just run."),
    ("🤷 It's Fine", "You'll tolerate each other indefinitely."),
    ("✨ Soulmates", "Statistically unlikely. Congrats."),
    ("😬 Complicated", "It's a lot. Are you sure?"),
    ("🌙 Cosmic Chaos", "Nobody knows. The stars are confused."),
]

REJECTED_APP_IDEAS = [
    "Uber but for returning things you borrowed 2 years ago",
    "Tinder but for finding someone to kill the spider",
    "LinkedIn but only for naps",
    "Duolingo but for learning to say no",
    "Shazam but for identifying the smell in your car",
    "Google Maps but it only shows you restaurants you've already been to",
    "Airbnb but for borrowing someone's couch for one specific Tuesday",
    "Netflix but it picks for you and you can't argue",
]

PASSIVE_AGGRESSIVE_NOTES = [
    "To whoever keeps taking my lunch from the fridge: I hope it was worth it. I hope you think about this.",
    "Friendly reminder that the dishwasher is not, and has never been, a storage unit.",
    "The wifi password has been changed. You know what you did.",
    "Just a note: 'reply all' is a privilege, not a right.",
    "This is a gentle reminder that 'working from home' and 'being home' are not the same.",
    "To the person who uses the last of something and puts the empty container back: we need to talk.",
]

ANIMALS_AS_COWORKERS = [
    ("🐈 Cat", "Does exactly what they want. Unmanageable. Everyone loves them anyway."),
    ("🐕 Dog", "Too enthusiastic in every meeting. Brings energy. Smells slightly off."),
    ("🐧 Penguin", "Formal at all times. Never explains why. Extremely organized."),
    ("🦦 Otter", "Holds your hand during stressful meetings. Floats through deadlines."),
    ("🦥 Sloth", "Will get to it. Has said this since Q1. Still getting to it."),
    ("🐸 Frog", "Contributes nothing but sits in the corner and vibes. Essential."),
    ("🦜 Parrot", "Repeats everything you say in the all-hands. Somehow gets promoted."),
    ("🐻 Bear", "Hibernates November through March. Emails say 'OOO indefinitely'."),
]

PROCRASTINATION_STAGES = [
    "Stage 1: You notice the task exists. You close the tab.",
    "Stage 2: You think about the task. You make a snack instead.",
    "Stage 3: You make a detailed plan to do the task. The plan counts as doing it.",
    "Stage 4: You tell someone about the task. They say 'wow'. You feel accomplished.",
    "Stage 5: You open the task. You close it. You watch a documentary.",
    "Stage 6: It's due tomorrow. Adrenaline enters the chat.",
    "Stage 7: You do the task in 45 minutes. It was fine. It was always fine.",
    "Stage 8: You swear you'll start earlier next time.",
]

UNSOLICITED_OPINIONS = [
    "Pineapple on pizza is fine and you know it.",
    "The Lord of the Rings could have been one movie.",
    "Cargo shorts are objectively practical and the hate is personal.",
    "We're all pretending socks are comfortable and nobody is saying anything.",
    "Ranch dressing goes on everything. This is not up for debate.",
    "The word 'moist' is perfectly fine and you're overreacting.",
    "Reply-all is never necessary and yet here we are every single day.",
    "Brunch is just breakfast with a superiority complex.",
]

EMOJI_TRANSLATOR = [
    ("👁️👄👁️", "I am watching. I am concerned. I cannot look away."),
    ("💀", "I am deceased from this information."),
    ("😭", "This is extremely funny. I am not sad."),
    ("🫠", "I am melting due to stress, heat, or secondhand embarrassment."),
    ("🧍", "I am standing here. Having a normal one. Not okay."),
    ("🗿", "I have no reaction left. I am stone. I am done."),
    ("🤌", "Italian emphasis. Perfection. Could also mean 'what do you want'."),
    ("✨", "Either very positive OR deeply sarcastic. Context required."),
    ("😌", "I have decided I am unbothered. I am still bothered."),
    ("🫡", "Yes sir. Understood. Will not do that."),
]

FAKE_HISTORY = [
    "On this day: someone invented the word 'fine' to avoid explaining how they actually felt.",
    "On this day: the first person to say 'we should do this more often' immediately never did.",
    "On this day: left-on-read was discovered. Nobody recovered.",
    "On this day: someone replied 'haha' to end a conversation and it worked.",
    "On this day: the group chat went quiet forever. No explanation. None needed.",
    "On this day: someone said 'I'll sleep when I'm dead' and then slept for 11 hours.",
    "On this day: autocorrect changed 'I'm on my way' to something catastrophic.",
    "On this day: the first 'per my last email' was sent. The internet has never been the same.",
]

BINGO_PHRASES = [
    "circle back", "synergy", "bandwidth", "deep dive", "move the needle",
    "low-hanging fruit", "pain point", "pivot", "leverage", "going forward",
    "touch base", "take this offline", "unpack", "drill down", "boil the ocean",
    "paradigm shift", "holistic", "scalable", "agile", "value add",
    "actionable", "ideate", "disruptive", "best practice", "swim lane",
]

POSTER_TEXTS = [
    ("PERSISTENCE", "The ability to keep doing something that isn't working."),
    ("TEAMWORK", "Sharing the blame evenly among several people."),
    ("EXCELLENCE", "Doing slightly more than the bare minimum, occasionally."),
    ("VISION", "Looking confidently in the wrong direction."),
    ("SYNERGY", "When two people do one job that one person should do."),
    ("LEADERSHIP", "Walking slightly ahead and hoping others follow."),
    ("INNOVATION", "Repackaging existing things and calling them new."),
    ("HUSTLE", "The art of being tired but smiling about it."),
]

# ============ SESSION STATE ============

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
    "current_excuse": None,
    "current_conspiracy": None,
    "proc_stage": 0,
    "bingo_card": random.sample(BINGO_PHRASES, 16),
    "bingo_marked": set(),
    "final_clicked": 0,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ============ HELPER ============

def section(num, title, cap=None):
    st.markdown(f"**— {str(num).zfill(2)} —**")
    st.subheader(title)
    if cap:
        st.caption(cap)

# ============ HEADER ============

st.markdown('<div class="big-title">DUMB<br>STUFF</div>', unsafe_allow_html=True)
st.caption("50 features · zero purpose · you're very welcome")
st.markdown("---")

# ===== 01 =====
section(1, "Useless Facts")
st.info(f"**FACT:** {FACTS[st.session_state.fact_idx]}")
if st.button("Give me another →", key="fact_btn"):
    st.session_state.fact_idx = (st.session_state.fact_idx + 1) % len(FACTS)
    st.rerun()
st.markdown("---")

# ===== 02 =====
section(2, "Unsolicited Compliments")
if st.button("Compliment me 🙏", key="compliment_btn"):
    st.success(f"**YOU:** {random.choice(COMPLIMENTS)}")
st.markdown("---")

# ===== 03 =====
section(3, "Excuse Generator")
if st.button("Generate Excuse", key="excuse_btn"):
    st.session_state.current_excuse = random.choice(EXCUSES)
if st.session_state.current_excuse:
    st.warning(f"**EXCUSE:** {st.session_state.current_excuse}")
    st.code(st.session_state.current_excuse, language=None)
    st.caption("☝️ click the copy icon on the right")
st.markdown("---")

# ===== 04 =====
section(4, "Button That Does Nothing", "this button does absolutely nothing")
if st.button("DO NOT PRESS", key="nothing_btn"):
    st.session_state.nothing_clicks += 1
if st.session_state.nothing_clicks > 0:
    n = st.session_state.nothing_clicks
    msg = NOTHING_BUTTON_RESPONSES[min(n - 1, len(NOTHING_BUTTON_RESPONSES) - 1)]
    st.error(f"{msg}{' (×' + str(n) + ')' if n > 9 else ''}")
st.markdown("---")

# ===== 05 =====
section(5, "Roast Generator")
if st.button("🔥 Roast Me", key="roast_btn"):
    st.error(f"🔥 {random.choice(ROASTS)}")
st.markdown("---")

# ===== 06 =====
section(6, "Life Advice Dispenser", "shake the magic 8-ball of mediocre wisdom")
if st.button("🔮 Dispense Wisdom", key="advice_btn"):
    with st.spinner("shaking..."):
        time.sleep(0.4)
    st.info(f"🔮 {random.choice(LIFE_ADVICE)}")
st.markdown("---")

# ===== 07 =====
section(7, "Psychic Predictions", "the oracle sees all. all is mundane.")
if st.button("🔭 Predict My Future", key="predict_btn"):
    with st.spinner("consulting the vibes..."):
        time.sleep(0.6)
    st.info(f"🔭 {random.choice(PREDICTIONS)}")
st.markdown("---")

# ===== 08 =====
section(8, "Would You Rather", "no wrong answer (there is a wrong answer)")
pair = WOULD_YOU_RATHER[st.session_state.wyr_idx]
col1, col2 = st.columns(2)
with col1:
    if st.button(f"A: {pair[0]}", key="wyr_a"):
        st.session_state.wyr_choice = 0
with col2:
    if st.button(f"B: {pair[1]}", key="wyr_b"):
        st.session_state.wyr_choice = 1
if st.session_state.wyr_choice is not None:
    st.success(f"You chose: **{pair[st.session_state.wyr_choice]}**. Fascinating.")
    if st.button("Next Dilemma →", key="wyr_next"):
        st.session_state.wyr_idx = (st.session_state.wyr_idx + 1) % len(WOULD_YOU_RATHER)
        st.session_state.wyr_choice = None
        st.rerun()
st.markdown("---")

# ===== 09 =====
section(9, "Conspiracy Corner", "100% true, probably")
if st.button("🤫 Expose The Truth", key="conspiracy_btn"):
    st.session_state.current_conspiracy = random.choice(CONSPIRACIES)
if st.session_state.current_conspiracy:
    st.warning(f"🤫 {st.session_state.current_conspiracy}")
st.markdown("---")

# ===== 10 =====
section(10, "Haiku of the Moment", "5-7-5 syllables of truth")
if st.button("Generate Haiku", key="haiku_btn"):
    h = random.choice(HAIKUS)
    st.markdown(f"> *{h[0]}*  \n> *{h[1]}*  \n> *{h[2]}*")
st.markdown("---")

# ===== 11 =====
section(11, "Vibe Check", "scientifically certified results")
if st.button("Check My Vibe", key="vibe_btn"):
    with st.spinner("scanning..."):
        time.sleep(1)
    emoji, label, desc = random.choice(VIBE_CHECKS)
    st.markdown(f"### {emoji} {label}")
    st.info(desc)
st.markdown("---")

# ===== 12 =====
section(12, "NPC Encounter", "press A to interact")
if st.button("▶ Press A", key="npc_btn"):
    st.code(f"VILLAGER: {random.choice(NPC_LINES)}", language=None)
st.markdown("---")

# ===== 13 =====
section(13, "Truth or Dare", "internet edition")
col1, col2 = st.columns(2)
with col1:
    truth_btn = st.button("Truth", key="truth_btn")
with col2:
    dare_btn = st.button("Dare", key="dare_btn")
if truth_btn:
    _, q = random.choice([(t, q) for t, q in TRUTH_OR_DARE if t == "truth"])
    st.error(f"**TRUTH:** {q}")
if dare_btn:
    _, q = random.choice([(t, q) for t, q in TRUTH_OR_DARE if t == "dare"])
    st.warning(f"**DARE:** {q}")
st.markdown("---")

# ===== 14 =====
section(14, "Personality Breakdown", "based on nothing")
if st.button("Analyze Me", key="personality_btn"):
    with st.spinner("analyzing your entire being..."):
        time.sleep(1.5)
    for trait in PERSONALITY_TRAITS:
        val = random.randint(10, 99)
        st.text(f"{trait} — {val}%")
        st.progress(val / 100)
st.markdown("---")

# ===== 15 =====
section(15, "Mood → Playlist", "vibes only, no links, you figure it out")
mood_options = [f"{e} {l}" for e, l, _ in MOODS]
selected_mood = st.radio("pick your mood:", mood_options, key="mood_radio", label_visibility="collapsed")
if selected_mood:
    idx = mood_options.index(selected_mood)
    st.success(f"**Listen to:** {MOODS[idx][2]}")
st.markdown("---")

# ===== 16 =====
section(16, "Countdown to Nothing", "meaningless events, precisely timed")
events = {"end of this sentence": 5, "next awkward silence": 12, "you forgetting this website exists": 30, "an email you'll ignore": 60}
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
    status.success("✓ it happened. nothing changed.")
st.markdown("---")

# ===== 17 =====
section(17, "Bad Decision Hotline", "staffed by nobody qualified")
if st.button("📞 Call The Hotline", key="hotline_btn"):
    with st.spinner("📞 ringing... hold music: gentle bossa nova"):
        time.sleep(1.8)
    st.info(f"**HOTLINE:** {random.choice(HOTLINE_RESPONSES)}")
st.markdown("---")

# ===== 18 =====
section(18, "Clicker Game", "the whole genre reduced to 1 section")
st.metric("Score", st.session_state.clicker_score, delta=f"×{st.session_state.clicker_multiplier} per click")
upgrade_cost = (st.session_state.clicker_upgrades + 1) * 50
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👆 CLICK", key="clicker_btn"):
        st.session_state.clicker_score += st.session_state.clicker_multiplier
        st.rerun()
with col2:
    if st.button(f"Upgrade (costs {upgrade_cost})", key="upgrade_btn", disabled=st.session_state.clicker_score < upgrade_cost):
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

# ===== 19 =====
section(19, "Soundboard (No Sound)", "your device does the sound (it doesn't)")
sounds = ["🎺", "🥁", "🎸", "🎹", "🎻", "📯"]
cols = st.columns(len(sounds))
for i, (col, sound) in enumerate(zip(cols, sounds)):
    with col:
        if st.button(sound, key=f"sound_{i}"):
            st.caption(f"{sound} → in your heart")
st.markdown("---")

# ===== 20 =====
section(20, "Wikipedia Rabbit Hole Simulator", "escape is optional")
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
            st.success(f"Escaped in {elapsed}s. Impressive.")
    with col2:
        if st.button("🕳️ I Fell In", key="wiki_fell"):
            st.session_state.wiki_running = False
            st.error(f"Fell in at {elapsed}s. Respectable.")
    st.button("🔄 Refresh Timer", key="wiki_refresh")
st.markdown("---")

# ===== 21 =====
section(21, "Professional Apology Generator", "sorry. kind of.")
if st.button("Generate Apology 🙏", key="apology_btn"):
    st.info(f"🙏 {random.choice(APOLOGIES)}")
st.markdown("---")

# ===== 22 =====
section(22, "Fake Job Title Generator", "for your email signature")
if st.button("What's My Title?", key="job_btn"):
    title = random.choice(JOB_TITLES)
    st.success(f"**Your official title:** {title}")
    st.code(title, language=None)
    st.caption("☝️ paste into LinkedIn immediately")
st.markdown("---")

# ===== 23 =====
section(23, "Red Flag Detector", "entirely subjective, probably accurate")
if st.button("🚩 Show Red Flag", key="redflag_btn"):
    st.error(f"🚩 {random.choice(RED_FLAGS)}")
st.markdown("---")

# ===== 24 =====
section(24, "Green Flag Appreciation", "celebrate the rare ones")
if st.button("🟢 Show Green Flag", key="greenflag_btn"):
    st.success(f"🟢 {random.choice(GREEN_FLAGS)}")
st.markdown("---")

# ===== 25 =====
section(25, "Shower Thought Dispenser", "arrives uninvited at 8am")
if st.button("🚿 Have a Thought", key="shower_btn"):
    with st.spinner("water is running..."):
        time.sleep(0.5)
    st.info(f"💭 {random.choice(SHOWER_THOUGHTS)}")
st.markdown("---")

# ===== 26 =====
section(26, "Dumb Horoscope", "the stars have opinions. they are wrong.")
star_sign = st.selectbox("your sign:", list(STAR_SIGNS_DUMB.keys()), key="sign_select")
if st.button("Read My Horoscope", key="horoscope_btn"):
    st.warning(f"**{star_sign}:** {STAR_SIGNS_DUMB[star_sign]}")
st.markdown("---")

# ===== 27 =====
section(27, "Fake Awards Ceremony", "recognition you didn't ask for")
if st.button("🏆 Present My Award", key="award_btn"):
    with st.spinner("drumroll..."):
        time.sleep(1)
    st.success(random.choice(FAKE_AWARDS))
st.markdown("---")

# ===== 28 =====
section(28, "Cursed Restaurant Menu", "fine dining for the confused")
if st.button("📋 Show Today's Special", key="menu_btn"):
    st.info(f"🍽️ **{random.choice(CURSED_MENU_ITEMS)}**")
st.markdown("---")

# ===== 29 =====
section(29, "Loading Screen Generator", "for when you need an excuse to stare at a screen")
if st.button("⏳ Generate Loading Screen", key="loading_btn"):
    msg = random.choice(LOADING_SCREENS)
    with st.spinner(msg):
        time.sleep(2)
    st.success("Done. Nothing loaded. As expected.")
st.markdown("---")

# ===== 30 =====
section(30, "Band Name Generator", "your future band awaits")
if st.button("🎸 Generate Band Name", key="band_btn"):
    name = f"{random.choice(BAND_NAME_PARTS_A)} {random.choice(BAND_NAME_PARTS_B)}"
    st.success(f"**Your band name:** {name}")
    st.code(name, language=None)
    st.caption("☝️ available on all streaming platforms (not really)")
st.markdown("---")

# ===== 31 =====
section(31, "Fortune Cookie Machine", "wisdom wrapped in a cookie")
if st.button("🥠 Crack Open Cookie", key="fortune_btn"):
    with st.spinner("cracking..."):
        time.sleep(0.6)
    st.info(f"🥠 *{random.choice(FORTUNE_COOKIES)}*")
st.markdown("---")

# ===== 32 =====
section(32, "Wrong Answer Only", "certified incorrect information")
if st.button("❓ Ask a Question", key="wrong_btn"):
    q, a = random.choice(WRONG_ANSWERS)
    st.markdown(f"**Q:** {q}")
    st.error(f"**A:** {a}")
st.markdown("---")

# ===== 33 =====
section(33, "Zodiac Compatibility Check", "are you compatible? probably not.")
col1, col2 = st.columns(2)
with col1:
    sign1 = st.selectbox("Person A:", list(STAR_SIGNS_DUMB.keys()), key="compat_a")
with col2:
    sign2 = st.selectbox("Person B:", list(STAR_SIGNS_DUMB.keys()), key="compat_b")
if st.button("Check Compatibility", key="compat_btn"):
    with st.spinner("consulting the cosmos..."):
        time.sleep(1)
    label, desc = random.choice(ZODIAC_COMPATIBILITY)
    st.markdown(f"### {label}")
    st.info(f"**{sign1} + {sign2}:** {desc}")
st.markdown("---")

# ===== 34 =====
section(34, "Rejected App Ideas", "silicon valley said no. correctly.")
if st.button("💡 Pitch an App", key="app_btn"):
    st.warning(f"📱 **App idea:** {random.choice(REJECTED_APP_IDEAS)}")
st.markdown("---")

# ===== 35 =====
section(35, "Passive Aggressive Note Generator", "for the office fridge")
if st.button("📝 Generate Note", key="passive_btn"):
    note = random.choice(PASSIVE_AGGRESSIVE_NOTES)
    st.error(f"📝 *{note}*")
    st.code(note, language=None)
    st.caption("☝️ print and post in breakroom")
st.markdown("---")

# ===== 36 =====
section(36, "Animal Coworker Personality", "which animal are you at work?")
if st.button("🐾 Find My Spirit Coworker", key="animal_btn"):
    with st.spinner("running the assessment..."):
        time.sleep(0.8)
    animal, desc = random.choice(ANIMALS_AS_COWORKERS)
    st.markdown(f"### {animal}")
    st.info(desc)
st.markdown("---")

# ===== 37 =====
section(37, "Procrastination Stage Checker", "where are you right now?")
st.info(PROCRASTINATION_STAGES[st.session_state.proc_stage])
st.caption(f"Stage {st.session_state.proc_stage + 1} of {len(PROCRASTINATION_STAGES)}")
col1, col2 = st.columns(2)
with col1:
    if st.button("Next Stage →", key="proc_next"):
        st.session_state.proc_stage = (st.session_state.proc_stage + 1) % len(PROCRASTINATION_STAGES)
        st.rerun()
with col2:
    if st.button("Reset to Stage 1", key="proc_reset"):
        st.session_state.proc_stage = 0
        st.rerun()
st.markdown("---")

# ===== 38 =====
section(38, "Unsolicited Opinion Dispenser", "nobody asked. here it is.")
if st.button("💬 Give Me Your Take", key="opinion_btn"):
    st.warning(f"🎤 {random.choice(UNSOLICITED_OPINIONS)}")
st.markdown("---")

# ===== 39 =====
section(39, "Emoji Translator", "what did they actually mean?")
emoji_options = [e for e, _ in EMOJI_TRANSLATOR]
selected_emoji = st.selectbox("pick an emoji:", emoji_options, key="emoji_select")
if st.button("🔍 Translate", key="emoji_btn"):
    meaning = dict(EMOJI_TRANSLATOR)[selected_emoji]
    st.info(f"**{selected_emoji}** means: *{meaning}*")
st.markdown("---")

# ===== 40 =====
section(40, "This Day in Fake History", "completely made up")
today = datetime.date.today()
random.seed(today.toordinal())
fake_event = random.choice(FAKE_HISTORY)
random.seed()
st.info(f"📅 **{today.strftime('%B %d')}:** {fake_event}")
st.markdown("---")

# ===== 41 =====
section(41, "Excuse Tier List", "objectively ranked")
tier_excuses = [
    ("S", "My pet needed emotional support"),
    ("A", "Traffic (there was no traffic)"),
    ("B", "I forgot"),
    ("C", "My alarm didn't go off"),
    ("D", "I was busy (I was not busy)"),
    ("F", "Mercury retrograde"),
]
for tier, excuse in tier_excuses:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{tier} tier**")
    with col2:
        st.caption(excuse)
st.markdown("---")

# ===== 42 =====
section(42, "Coin Flip (High Stakes Edition)")
if st.button("🪙 Flip Coin", key="coin_btn"):
    with st.spinner("flipping..."):
        time.sleep(0.5)
    result = random.choice(["HEADS", "TAILS"])
    commentary = random.choice([
        "The universe has spoken. You may now ignore it.",
        "Binding decision. No take-backs.",
        "Fate has chosen. Fate does not care.",
        "There it is. Do with this what you will.",
    ])
    st.success(f"**{result}** — {commentary}")
st.markdown("---")

# ===== 43 =====
section(43, "Random Number (Very Important)")
col1, col2 = st.columns(2)
with col1:
    low = st.number_input("from:", value=1, key="rng_low")
with col2:
    high = st.number_input("to:", value=100, key="rng_high")
if st.button("🎲 Generate Number", key="rng_btn"):
    if int(low) >= int(high):
        st.error("the second number needs to be bigger. just a thought.")
    else:
        n = random.randint(int(low), int(high))
        st.markdown(f"# {n}")
        st.caption("chosen by chaos. use it wisely.")
st.markdown("---")

# ===== 44 =====
section(44, "Meeting Bingo", "survive your next call")
if st.button("New Card 🔀", key="bingo_new"):
    st.session_state.bingo_card = random.sample(BINGO_PHRASES, 16)
    st.session_state.bingo_marked = set()
    st.rerun()
grid = [st.session_state.bingo_card[i:i+4] for i in range(0, 16, 4)]
for row_idx, row in enumerate(grid):
    cols = st.columns(4)
    for col_idx, (col, phrase) in enumerate(zip(cols, row)):
        with col:
            marked = phrase in st.session_state.bingo_marked
            label = f"✅ {phrase}" if marked else phrase
            if st.button(label, key=f"bingo_{row_idx}_{col_idx}"):
                if marked:
                    st.session_state.bingo_marked.discard(phrase)
                else:
                    st.session_state.bingo_marked.add(phrase)
                st.rerun()
st.caption(f"{len(st.session_state.bingo_marked)}/16 buzzwords survived")
st.markdown("---")

# ===== 45 =====
section(45, "Ye Olde Text Translator", "thine words, but medieval")
def ye_olde(text):
    replacements = {
        "you": "thee", "your": "thy", "are": "art", "is": "doth be",
        "the": "ye", "have": "hast", "do": "dost", "will": "shalt",
        "hello": "hail", "hi": "good morrow", "yes": "aye", "no": "nay",
        "very": "most", "really": "verily", "ok": "as thou wishest",
        "friend": "companion", "cool": "most excellent", "bad": "foul",
        "good": "noble", "go": "venture forth", "here": "hither",
        "there": "thither", "now": "presently", "later": "henceforth",
    }
    words = text.lower().split()
    result = []
    for word in words:
        clean = word.strip(".,!?;:'\"")
        punct = word[len(clean):]
        result.append(replacements.get(clean, clean) + punct)
    return " ".join(result)
olde_input = st.text_input("type something modern:", key="olde_input", placeholder="hey what are you doing later")
if olde_input:
    st.success(f"📜 *{ye_olde(olde_input)}*")
st.markdown("---")

# ===== 46 =====
section(46, "Complaint Department", "we hear you. we cannot help.")
complaint = st.text_area("lodge your complaint:", key="complaint_input", placeholder="the coffee machine is broken again", height=80)
if st.button("📮 Submit Complaint", key="complaint_btn"):
    if complaint:
        responses = [
            "Complaint received. Filed under: noted.",
            "Escalated to the team. The team is one pigeon.",
            "Your feedback is important. It has been placed in the correct bin.",
            "Forwarded to the relevant department. They're on vacation.",
            "Acknowledged and ignored. Thank you for your submission.",
            "We will not be changing anything. Sorry you feel this way.",
        ]
        st.info(f"📋 **Response:** {random.choice(responses)}")
    else:
        st.warning("you have to actually complain about something.")
st.markdown("---")

# ===== 47 =====
section(47, "Nap Duration Advisor", "science-based (not science-based)")
energy = st.slider("current energy level:", 0, 10, 5, key="energy_slider")
if st.button("💤 Advise My Nap", key="nap_btn"):
    if energy <= 2:
        st.error("**Recommended:** 8–10 hours. That's just sleep. Go to bed.")
    elif energy <= 5:
        st.warning("**Recommended:** 90 minutes. One full sleep cycle. Commit.")
    elif energy <= 7:
        st.info("**Recommended:** 20 minutes. Classic power nap. Set 2 alarms.")
    else:
        st.success("**Recommended:** You don't need one. But you'll take one anyway.")
st.markdown("---")

# ===== 48 =====
section(48, "Name a Price for Your Soul", "negotiation simulator")
soul_offer = st.number_input("your asking price ($):", min_value=0, value=500, step=100, key="soul_input")
if st.button("💼 Negotiate", key="soul_btn"):
    if soul_offer == 0:
        st.error("Giving it away for free? Have some self respect.")
    elif soul_offer < 100:
        st.error("Insulting. Absolutely insulting.")
    elif soul_offer < 1000:
        st.warning("Low. We were thinking more. Know your worth.")
    elif soul_offer < 10000:
        st.info("Reasonable. Management is unavailable. Will follow up.")
    elif soul_offer < 1000000:
        st.success("Now we're talking. Paperwork incoming. Please hold.")
    else:
        st.success("Deal. Nobody wanted it anyway. Congratulations.")
st.markdown("---")

# ===== 49 =====
section(49, "Motivational Poster (Bad)", "hang this in your cubicle")
if st.button("🖼️ Generate Poster", key="poster_btn"):
    word, subtext = random.choice(POSTER_TEXTS)
    st.markdown(f"---\n### ✦ {word} ✦\n*\"{subtext}\"*\n\n---")
st.markdown("---")

# ===== 50 =====
section(50, "The Final Button", "you've reached the end.")
if st.button("🎉 THE FINAL BUTTON", key="final_btn"):
    st.session_state.final_clicked += 1
    st.rerun()
if st.session_state.final_clicked == 0:
    st.caption("go on then.")
elif st.session_state.final_clicked == 1:
    st.balloons()
    st.success("🎉 You reached the end of a website called Dumb Stuff. Incredible.")
elif st.session_state.final_clicked == 2:
    st.snow()
    st.info("you pressed it again. here is snow.")
elif st.session_state.final_clicked == 3:
    st.warning("third time. you have a lot of free time. respect.")
else:
    st.error(f"you have pressed this {st.session_state.final_clicked} times. please go outside.")

# ============ FOOTER ============
st.markdown("---")
st.markdown(
    "<div style='text-align:center;font-family:monospace;font-size:11px;color:#bbb;letter-spacing:2px;'>"
    "© DUMB STUFF · 50 FEATURES · ALL RIGHTS RESERVED · NONE OF THIS MATTERS"
    "</div>",
    unsafe_allow_html=True
)
