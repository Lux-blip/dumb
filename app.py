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

# ============ FEATURES 51–100 ============

# ===== 51 =====
st.markdown("**— 51 —**")
st.subheader("Cursed Ice Breaker Questions")
st.caption("for meetings nobody wanted")
ICEBREAKERS = [
    "If your left shoe could talk, what would it say about you?",
    "What sound do you think the color blue makes?",
    "If procrastination were an Olympic sport, what would your medal ceremony look like?",
    "Describe your Monday using only condiments.",
    "If your sleep schedule were a country, what would its flag look like?",
    "What vegetable best represents your current emotional state?",
    "If your inbox were a natural disaster, what kind would it be?",
    "Rate your life as a Yelp review. One sentence only.",
    "What is the most aggressively mediocre thing about you?",
    "If your mood were a font, what font would it be and why is it Comic Sans?",
]
if st.button("🧊 Break the Ice", key="ice_btn"):
    st.info(f"❓ {random.choice(ICEBREAKERS)}")
st.markdown("---")

# ===== 52 =====
st.markdown("**— 52 —**")
st.subheader("Dramatic Narrator")
st.caption("your life, but cinematic")
NARRATOR_LINES = [
    "Little did they know, this would be the last time they checked their email before 10am.",
    "She opened the fridge. It was empty. As it always had been. As it always would be.",
    "He said 'I'll just watch one more episode.' History would remember this moment.",
    "The notification appeared at 11:47pm. It was a LinkedIn connection request.",
    "They had been staring at the cursor for 20 minutes. The document remained blank.",
    "She typed 'haha' but felt nothing.",
    "He refreshed the page. Still no reply. He refreshed again. This was his life now.",
    "The meeting began at 9. By 9:04, three souls had already left their bodies.",
    "She said 'sounds good' and immediately forgot what she had agreed to.",
    "He closed 47 tabs. Opened 52 new ones. Order had been restored.",
]
if st.button("🎬 Narrate My Life", key="narrator_btn"):
    with st.spinner("zooming in dramatically..."):
        time.sleep(0.7)
    st.info(f"🎙️ *{random.choice(NARRATOR_LINES)}*")
st.markdown("---")

# ===== 53 =====
st.markdown("**— 53 —**")
st.subheader("Unnecessary Warning Labels")
st.caption("for everyday objects that don't need them")
WARNINGS = [
    "⚠️ CHAIR: May cause sitting. Prolonged use leads to being seated.",
    "⚠️ MIRROR: Reflection may not match self-perception. Consult therapist.",
    "⚠️ COFFEE MUG: Contains hot liquid. You know this. You always do this anyway.",
    "⚠️ ALARM CLOCK: Will cause morning. Cannot be held liable for Monday.",
    "⚠️ PHONE: Prolonged use may result in knowing things you didn't want to know.",
    "⚠️ PILLOW: Extremely comfortable. May render user non-functional.",
    "⚠️ FRIDGE: Opens easily. Closes in disappointment. Cycle repeats.",
    "⚠️ CALENDAR: Contains dates. Some of these dates have things on them. You forgot.",
    "⚠️ NOTEBOOK: 97% probability of remaining blank. Handle with low expectations.",
    "⚠️ WIFI ROUTER: Turning off and on again will fix it. You will try everything else first.",
]
if st.button("⚠️ Generate Warning", key="warning_btn"):
    st.warning(random.choice(WARNINGS))
st.markdown("---")

# ===== 54 =====
st.markdown("**— 54 —**")
st.subheader("Villain Origin Story Generator")
st.caption("everyone has one")
VILLAIN_ORIGINS = [
    "It started the day the printer said it was out of ink. It was not out of ink.",
    "The turning point was when someone put a reply-all on a 200-person email chain. Twice.",
    "They were normal once. Then someone ate their clearly labeled lunch from the office fridge.",
    "The descent began with a software update that moved the button they used every day.",
    "It was the third time in a row that their headphones got tangled in under 10 seconds.",
    "One day, someone said 'can you hear me?' on a call. Then said it again. Then again.",
    "The moment the self-checkout machine said 'unexpected item in bagging area' for no reason.",
    "It was the day they had to explain, for the fifth time, how to attach a file to an email.",
    "The WiFi dropped mid-upload. The file was gone. They were never the same.",
    "They had been put on hold for 47 minutes. The hold music was a pan flute rendition of Havana.",
]
if st.button("😈 Generate Origin Story", key="villain_btn"):
    with st.spinner("descending into darkness..."):
        time.sleep(0.8)
    st.error(f"😈 {random.choice(VILLAIN_ORIGINS)}")
st.markdown("---")

# ===== 55 =====
st.markdown("**— 55 —**")
st.subheader("Extremely Specific Compliments")
st.caption("hyper-targeted validation")
SPECIFIC_COMPLIMENTS = [
    "The way you close a bag of chips before putting it back is genuinely admirable.",
    "Your specific walk to the kitchen at 11pm shows real character.",
    "The face you make when pretending to understand something is incredibly convincing.",
    "Your method of ignoring notifications is an art form.",
    "The pause before you answer a question makes you seem extremely wise.",
    "Your ability to find the exact right meme at the exact right moment is a gift.",
    "The noise you make when you sit down has a lot of personality.",
    "The way you say 'hm' while reading something is genuinely compelling.",
    "Your technique for pretending to be busy is top tier.",
    "The face you make when something loads slowly deserves its own exhibit.",
]
if st.button("🎯 Compliment Me Specifically", key="specific_btn"):
    st.success(f"✨ {random.choice(SPECIFIC_COMPLIMENTS)}")
st.markdown("---")

# ===== 56 =====
st.markdown("**— 56 —**")
st.subheader("Text Message Tone Analyzer")
st.caption("what did they REALLY mean")
TONES = [
    ("'k'", "They are fine. They are NOT fine. Tread carefully."),
    ("'ok!'", "Aggressively pleasant. Something is wrong."),
    ("'haha'", "This was not funny to them. This ended the conversation."),
    ("'no worries!'", "There are worries. Significant worries."),
    ("'sounds good'", "They stopped reading after the first sentence."),
    ("'sure'", "They do not want to. They will do it anyway. Resentfully."),
    ("'lol'", "Could mean anything. Unknowable. Do not ask for clarification."),
    ("'noted'", "Filed under: will not act on this."),
    ("'...'", "They are typing. They deleted it. You will never know what it said."),
    ("'per my last email'", "They are composed on the outside. Not on the inside."),
]
if st.button("📱 Analyze a Message", key="tone_btn"):
    text, analysis = random.choice(TONES)
    st.markdown(f"**Message:** {text}")
    st.info(f"**What it means:** {analysis}")
st.markdown("---")

# ===== 57 =====
st.markdown("**— 57 —**")
st.subheader("Overheard at the Office")
st.caption("actual sentences that were said by real humans")
OVERHEARD = [
    "'We need to blue-sky this and then circle back with a 30,000 foot view.'",
    "'Let's not boil the ocean here, just move the needle on the low-hanging fruit.'",
    "'I want to take this offline but also online. Both. Neither. I'll send a calendar invite.'",
    "'Can we get alignment on this before we get alignment on this?'",
    "'Going forward, going backward is no longer an option.'",
    "'We're pivoting our pivot strategy to be more agile about our agility.'",
    "'Let's not reinvent the wheel but also let's completely reinvent the wheel.'",
    "'I don't have bandwidth for this right now, but I also don't have bandwidth to say I don't have bandwidth.'",
    "'This is a solution in search of a problem, and the problem is that we have no solution.'",
    "'Let's take a step back to take two steps forward by stepping sideways.'",
]
if st.button("👂 What Did They Say", key="overheard_btn"):
    st.warning(f"💬 {random.choice(OVERHEARD)}")
st.markdown("---")

# ===== 58 =====
st.markdown("**— 58 —**")
st.subheader("The 'Is It a Red Flag or Just a Tuesday' Classifier")
st.caption("nuance machine")
CLASSIFIER = [
    ("Hasn't texted back in 3 days", "Red flag OR they lost their phone OR they are living their life. Spin a wheel."),
    ("Owns 14 candles", "Green flag. Ambiance is a value."),
    ("Uses dark mode on everything", "Neutral. Millions of people do this. You also do this."),
    ("Has seen every Marvel movie twice", "That's just time management. Jury's out."),
    ("Alphabetizes their spices", "Concerning OR extremely organized. Could go either way."),
    ("Takes 45 minutes to order coffee", "Red flag OR they really care about coffee. Which is also a flag."),
    ("Hasn't updated their phone in 2 years", "Chaotic neutral. Respect."),
    ("Cries at commercials", "Green flag. They feel things. Rare."),
    ("Has a 'work playlist' with 1 song on it", "Normal. The song is probably Mr. Brightside."),
    ("Refers to their cat as their 'child'", "No notes. Correct behavior."),
]
if st.button("🔎 Classify the Behavior", key="classifier_btn"):
    behavior, verdict = random.choice(CLASSIFIER)
    st.markdown(f"**Behavior:** {behavior}")
    st.info(f"**Verdict:** {verdict}")
st.markdown("---")

# ===== 59 =====
st.markdown("**— 59 —**")
st.subheader("Corporate Email Translator")
st.caption("decode the subtext")
CORP_EMAILS = [
    ("As per my previous email...", "You ignored this. I am noting that you ignored this. For the record."),
    ("Hope this finds you well.", "I don't care how you are. Let's get to it."),
    ("Just checking in!", "You haven't responded in 6 days. This is the third follow-up."),
    ("Thanks for your patience.", "This took way too long and we both know it."),
    ("Going forward...", "You messed up. We won't say that. But: you messed up."),
    ("I wanted to loop you in.", "You're being CC'd so you can't say you didn't know."),
    ("Let me know if you have any questions.", "Please don't have any questions."),
    ("As discussed...", "We said this out loud. I'm now writing it. For documentation purposes."),
    ("Happy to jump on a call!", "I do not want to jump on a call."),
    ("Friendly reminder...", "Not friendly. A reminder. Framed as friendly to soften the passive aggression."),
]
if st.button("📧 Translate an Email", key="email_btn"):
    phrase, translation = random.choice(CORP_EMAILS)
    st.markdown(f"**They wrote:** *\"{phrase}\"*")
    st.error(f"**They meant:** {translation}")
st.markdown("---")

# ===== 60 =====
st.markdown("**— 60 —**")
st.subheader("Cryptid Name Generator")
st.caption("what would your cryptid name be")
CRYPTID_A = ["The", "A", "Old", "Swamp", "Midnight", "Hollow", "Shadowed", "The Wandering"]
CRYPTID_B = ["Whispering", "Lurking", "Forgotten", "Pale", "Damp", "Restless", "Blinking", "Shuffling"]
CRYPTID_C = ["One", "Figure", "Shape", "Presence", "Thing", "Entity", "Creature", "Being"]
if st.button("👁️ Generate My Cryptid Name", key="cryptid_btn"):
    name = f"{random.choice(CRYPTID_A)} {random.choice(CRYPTID_B)} {random.choice(CRYPTID_C)}"
    st.success(f"**You are:** {name}")
    st.caption("spotted near the edge of a parking lot at 2am. several witnesses. no photos.")
st.markdown("---")

# ===== 61 =====
st.markdown("**— 61 —**")
st.subheader("What Energy Are You Giving Right Now")
st.caption("a scientific energy audit")
ENERGIES = [
    ("🧟 Zombie energy", "Functioning. Technically. The lights are on."),
    ("🌊 Flowing water energy", "Going wherever. Unbothered. Slightly dangerous."),
    ("🕯️ Single candle energy", "Warm. Flickering. Could go out at any moment."),
    ("🧲 Main character energy", "Everything revolves around you right now. You didn't ask for this."),
    ("🪨 Rock energy", "Immovable. Ancient. Not doing anything today."),
    ("🌀 Drain energy", "Spiraling slowly downward. It's fine. Drains are important."),
    ("📡 Signal energy", "Broadcasting constantly. Nobody is tuning in."),
    ("🧂 Salt energy", "Preservation mode. Slight bitterness. Long shelf life."),
    ("🌿 Houseplant energy", "Alive. Mostly. Needs water. Not asking for much."),
    ("⚡ Static electricity energy", "Unpredictable. Shocking to encounter. Attracted to carpets."),
]
if st.button("🔋 Audit My Energy", key="energy_btn"):
    with st.spinner("scanning your aura..."):
        time.sleep(0.8)
    label, desc = random.choice(ENERGIES)
    st.markdown(f"### {label}")
    st.info(desc)
st.markdown("---")

# ===== 62 =====
st.markdown("**— 62 —**")
st.subheader("Wrong Motivational Quote")
st.caption("inspiration, but incorrect")
WRONG_QUOTES = [
    "\"Every day is a gift.\" — The gift is non-returnable. No receipt.",
    "\"You miss 100% of the shots you don't take.\" — You also miss most of the ones you do take. Statistically.",
    "\"Be the change you wish to see in the world.\" — The world has not noticed.",
    "\"Work smarter, not harder.\" — Nobody has explained the difference yet.",
    "\"Your only limit is your mind.\" — Also time, money, sleep deprivation, and physics.",
    "\"Dream big.\" — Dreams are free. The rest is not.",
    "\"Good things come to those who wait.\" — Also bad things. Things just come. Timing is chaos.",
    "\"Everything happens for a reason.\" — The reason is usually a series of unrelated coincidences.",
    "\"Live, laugh, love.\" — In that order. Results not guaranteed.",
    "\"Today is the first day of the rest of your life.\" — Tomorrow also is. So is every day. That's how time works.",
]
if st.button("💬 Inspire Me Incorrectly", key="misquote_btn"):
    st.info(f"🌅 {random.choice(WRONG_QUOTES)}")
st.markdown("---")

# ===== 63 =====
st.markdown("**— 63 —**")
st.subheader("The Snack Oracle")
st.caption("what snack are you, spiritually")
SNACK_READINGS = [
    ("🥨 Pretzel", "Twisted but salty. A complex individual. Goes with everything. Underrated."),
    ("🍿 Popcorn", "Light until suddenly not. Unpredictable. Sometimes burns."),
    ("🧀 String Cheese", "Methodical. Likes to take things one layer at a time. People find this annoying."),
    ("🍫 Chocolate", "Smooth on the outside. Complicated within. Melts under pressure."),
    ("🥜 Peanut Butter", "Dense. Sticks to things. A lot going on. Best in small doses."),
    ("🌮 Chips and Salsa", "Can't stop at one. Addictive personality. The salsa is your inner life."),
    ("🍪 Cookie", "Warm, familiar, reliable. Occasionally crumbles. Still good."),
    ("🍉 Watermelon", "Great energy. Mostly water. Summer vibes only."),
    ("🧆 Hummus", "Earthy. Sophisticated surface. Requires others to function. The crackers are your support system."),
    ("🥐 Croissant", "High maintenance. Worth it. Takes forever. Worth it."),
]
if st.button("🔮 Consult the Snack Oracle", key="snack_btn"):
    with st.spinner("the oracle is considering..."):
        time.sleep(0.9)
    snack, reading = random.choice(SNACK_READINGS)
    st.markdown(f"### You are: {snack}")
    st.info(reading)
st.markdown("---")

# ===== 64 =====
st.markdown("**— 64 —**")
st.subheader("Overly Formal Letter for a Simple Request")
st.caption("when you need to ask someone to please stop microwaving fish")
FORMAL_LETTERS = [
    ("To Whoever Is Microwaving Fish",
     "Dear Occupant of the Second-Floor Kitchen,\n\nIt is with the utmost gravity that I write to formally request a cessation of the thermal preparation of aquatic protein in the shared microwave unit. The resulting aromatic emissions have been assessed as 'deeply personal' by affected parties.\n\nYours formally,\nA Colleague"),
    ("Regarding the Empty Toilet Paper Roll",
     "Dear Unknown Party,\n\nI write in a spirit of collegial cooperation to address a matter of some urgency. The cardboard cylinder which remains fixed to the holder does not, in fact, constitute a replacement. I respectfully request corrective action at your earliest convenience.\n\nWith restrained frustration,\nA Fellow Occupant"),
    ("Re: The Passive-Aggressive Dish Situation",
     "Dear Housemate or Colleague,\n\nI wish to draw your attention to the ceramic items currently residing in the sink, which have been there since Tuesday and may now qualify as permanent fixtures. Please advise on your intended timeline.\n\nRegards,\nThe Person Who Washed Their One Mug Around Them"),
]
if st.button("📜 Generate Formal Letter", key="formal_btn"):
    subject, body = random.choice(FORMAL_LETTERS)
    st.markdown(f"**RE: {subject}**")
    st.code(body, language=None)
st.markdown("---")

# ===== 65 =====
st.markdown("**— 65 —**")
st.subheader("Yelp Review for a Life Event")
st.caption("★★★☆☆")
YELP_REVIEWS = [
    "★★☆☆☆ — Monday. Came back again despite last week. Staff (alarm clock) aggressive. Coffee adequate. Would not recommend but will return.",
    "★★★★☆ — Nap. Arrived skeptical, stayed longer than intended. Atmosphere excellent. Slight grogginess upon exit. Would visit again.",
    "★☆☆☆☆ — Meeting that could have been an email. No parking. Ran over time. No snacks. Will not be back. Too late, already scheduled for Tuesday.",
    "★★★☆☆ — Grocery store at 6pm on a Sunday. Chaotic. Emotional. Ran into someone I went to school with. We both pretended not to see each other. Lost 2 stars.",
    "★★★★★ — Lying down on the couch. Exceptional value. Free. Highly accessible. 10/10 would do nothing again.",
    "★★☆☆☆ — Replying to a message I've been avoiding for 11 days. Stressful lead-up, anticlimactic resolution. The response was 'haha ok'. I have questions.",
    "★★★☆☆ — My own birthday. Didn't ask for this, came anyway. Cake was good. Had to be present the whole time. Mixed feelings. Will not repeat.",
]
if st.button("⭐ Write a Yelp Review", key="yelp_btn"):
    st.warning(f"📍 {random.choice(YELP_REVIEWS)}")
st.markdown("---")

# ===== 66 =====
st.markdown("**— 66 —**")
st.subheader("Out of Office Message Generator")
st.caption("for when you're gone and also when you're not")
OOO_MESSAGES = [
    "I am currently out of office, out of patience, and out of bandwidth. I will return when I have located at least one of these.",
    "I am away from my desk. My desk is not away from me. It follows me everywhere. But I will respond on Monday.",
    "Thank you for your email. I have received it. I have read it. I have not yet made peace with it. I will respond shortly.",
    "I am on vacation. I will see your email. I will think about it. I will respond when I am ready and not a moment before.",
    "I am currently attending a conference where I am learning things that could have been a document. I return Friday.",
    "I am out of the office until further notice. If this is urgent, please reconsider whether it is urgent.",
    "I will be away from email for the next several days. During this time I will be a slightly more functional version of myself.",
]
if st.button("✈️ Generate OOO Message", key="ooo_btn"):
    msg = random.choice(OOO_MESSAGES)
    st.info(f"📬 {msg}")
    st.code(msg, language=None)
st.markdown("---")

# ===== 67 =====
st.markdown("**— 67 —**")
st.subheader("Unnecessary Proverb Generator")
st.caption("old wisdom. new irrelevance.")
PROVERBS = [
    "A watched pot never boils, but an unwatched one will absolutely boil over and ruin your stove.",
    "The early bird gets the worm, but the second mouse gets the cheese. Choose your metaphor carefully.",
    "You can lead a horse to water but you cannot make it reply to your email within the hour.",
    "A rolling stone gathers no moss, but it does gather a lot of questions about its direction.",
    "People who live in glass houses shouldn't throw stones, but more urgently, they should invest in curtains.",
    "All that glitters is not gold. Some of it is very realistic glitter, which is worse.",
    "The pen is mightier than the sword, but the passive-aggressive email is mightier than both.",
    "Don't count your chickens before they hatch. Don't count them after either. Let the chickens have privacy.",
    "A bird in the hand is worth two in the bush, unless the bird is biting you, in which case let it go.",
    "Good things come to those who wait, but good things also come to those who act, so the proverb is not useful.",
]
if st.button("📖 Dispense Proverb", key="proverb_btn"):
    st.info(f"📜 {random.choice(PROVERBS)}")
st.markdown("---")

# ===== 68 =====
st.markdown("**— 68 —**")
st.subheader("Diagnosis: What Kind of Tired Are You")
st.caption("there are many kinds")
TIRED_TYPES = [
    ("😴 Regular Tired", "Needs sleep. Has not slept. Will not sleep yet."),
    ("🧠 Brain Tired", "Can't process simple things. Stared at a sentence for 4 minutes. Moved on."),
    ("👥 People Tired", "Technically fine. Just needs to not interact with anyone for 2-5 business days."),
    ("📋 Admin Tired", "Has 14 forms to fill out. Has opened them. Has closed them. Has opened them again."),
    ("🌍 Existentially Tired", "Functioning but questioning the broader context. Will be fine. Probably."),
    ("😤 Tired of a Specific Person", "You know who it is. They know who they are. Nothing will be said."),
    ("✅ Done-Everything Tired", "Rare. Productive. Earned. Take the nap."),
    ("🔄 Same Day Over and Over Tired", "Tuesday has happened several times this week already."),
    ("📱 Screen Tired", "Eyes like sandpaper. Has looked at a screen for 11 hours. Looking at one now."),
    ("🎭 Pretending-to-be-Fine Tired", "Performing wellness. The performance is convincing. The performer is tired."),
]
if st.button("😩 Diagnose My Tired", key="tired_btn"):
    with st.spinner("running diagnostics..."):
        time.sleep(0.6)
    kind, desc = random.choice(TIRED_TYPES)
    st.markdown(f"### Diagnosis: {kind}")
    st.info(desc)
st.markdown("---")

# ===== 69 =====
st.markdown("**— 69 —**")
st.subheader("The Museum of Minor Inconveniences")
st.caption("exhibits open daily")
EXHIBITS = [
    "🖼️ EXHIBIT 7A: *The Charger That Was Just Too Short* — oil on canvas, 2019. On permanent loan from the nightstand.",
    "🖼️ EXHIBIT 12: *The Bag That Ripped Right At the Bottom* — mixed media, eggs and other groceries.",
    "🖼️ EXHIBIT 3: *The Earphone That Stopped Working on One Side* — sound installation. Silence on the right.",
    "🖼️ EXHIBIT 19: *The Autocorrect That Changed the Wrong Word at the Wrong Time* — digital print. The recipient still has screenshots.",
    "🖼️ EXHIBIT 8: *The Cup That Dribbled Even Though It's a Normal Cup* — ceramic, somehow betrayal.",
    "🖼️ EXHIBIT 44: *The Parking Space That Was Almost Close* — site-specific installation, 1.5 blocks away.",
    "🖼️ EXHIBIT 2: *The Pen That Worked Yesterday* — performance art. Daily. Ongoing.",
    "🖼️ EXHIBIT 31: *The Chip Bag That Was 40% Air* — inflatable sculpture, false promises.",
]
if st.button("🏛️ View an Exhibit", key="museum_btn"):
    st.info(random.choice(EXHIBITS))
st.markdown("---")

# ===== 70 =====
st.markdown("**— 70 —**")
st.subheader("Your Protagonist Archetype")
st.caption("what trope are you in the movie of your life")
ARCHETYPES = [
    ("🕵️ The One Who Knows Too Much", "You've noticed things. You've said nothing. You're waiting for the right moment. It hasn't come."),
    ("😴 The Reluctant Hero", "You didn't ask for any of this. You will eventually do the thing. You need 20 more minutes first."),
    ("📚 The Wise Background Character", "You don't have the main plot. You have all the information the main character needs. Nobody asks."),
    ("🔁 The One Going Through a Montage", "Things are changing. There's music. You're not sure it's working. It might be working."),
    ("🚪 The Person Who Just Wants to Leave", "You have somewhere else to be. You've been at this party for 45 minutes too long."),
    ("🤝 The Loyal Sidekick Who Deserves Better", "You're doing 60% of the work. You're getting 0% of the credit. The sequel will correct this."),
    ("🌀 The Chaos Element", "You arrive and things happen. Not your fault. Technically your fault. Hard to prove."),
    ("😌 The Character Who Somehow Has It Together", "You appear calm. You are not calm. The appearance is load-bearing."),
]
if st.button("🎬 Find My Archetype", key="archetype_btn"):
    with st.spinner("analyzing the narrative arc of your life..."):
        time.sleep(1)
    kind, desc = random.choice(ARCHETYPES)
    st.markdown(f"### {kind}")
    st.info(desc)
st.markdown("---")

# ===== 71 =====
st.markdown("**— 71 —**")
st.subheader("Generic Social Media Caption Generator")
st.caption("for when you need words under the photo")
CAPTIONS = [
    "Chasing sunsets and good vibes ✨ [location TBD] [filter: whatever]",
    "Sometimes you just need to [activity]. 🙏 Grateful. Blessed. Caffeinated.",
    "Living, laughing, and occasionally functioning. #MondayMotivation #Actually It's Thursday",
    "Not all who wander are lost, but I definitely parked somewhere weird.",
    "This [object/place/food] understood the assignment. 💅",
    "POV: you're [doing thing] and [vague emotion] about it",
    "Soft life era. Nap era. Snack era. All the eras simultaneously.",
    "Just a [person/thing] standing in front of [other thing] asking it to [simple request].",
    "Main character behavior. Supporting character budget. 🎬",
    "No notes. [There are notes. I have notes. I am keeping them to myself.]",
]
if st.button("📸 Generate Caption", key="caption_btn"):
    st.success(f"✍️ {random.choice(CAPTIONS)}")
st.markdown("---")

# ===== 72 =====
st.markdown("**— 72 —**")
st.subheader("What Your Browser History Says About You")
st.caption("a character study")
BROWSER_HISTORIES = [
    "12:04am: 'is it normal to [thing]' — 12:05am: 'how common is [thing]' — 12:07am: '[celebrity] age' — 12:09am: 'what country has no extradition'",
    "'can dogs eat [food]' x7 — 'signs your dog is judging you' — 'do dogs have inner monologues' — 'dog therapist near me'",
    "'how to be productive' — 'why am I not productive' — 'famous people who were unproductive' — 'is being unproductive sometimes okay' — YouTube",
    "'what time does [place] close' — '[place] closed already' — 'places open near me right now' — 'cereal nutrition facts'",
    "'how to start a conversation' — 'how to end a conversation' — 'how to avoid conversations entirely' — 'remote jobs no talking required'",
    "'free things to do this weekend' — 'cheap things to do this weekend' — 'things to do this weekend' — 'things to do from couch' — Netflix",
    "'is [symptom] serious' — 'symptoms of [disease]' — 'do I have [disease]' — 'WebMD' — 'I'm fine actually' — 'calming playlists'",
]
if st.button("🔍 Reveal Browser History", key="browser_btn"):
    st.error(f"🕵️ *{random.choice(BROWSER_HISTORIES)}*")
st.markdown("---")

# ===== 73 =====
st.markdown("**— 73 —**")
st.subheader("The 'What's My Core Wound' Machine")
st.caption("extremely unqualified psychological assessment")
CORE_WOUNDS = [
    "Your core wound: someone once called you 'too much' and you've been 'not enough' ever since. The gap is interesting.",
    "Your core wound: you watched too many people be rewarded for being loud and now you're unsure if being thoughtful was a mistake.",
    "Your core wound: you said something vulnerable once and the room moved on very quickly. You have not said anything vulnerable since.",
    "Your core wound: you tried really hard at something and it didn't work and you haven't tried quite that hard again.",
    "Your core wound: someone important made you feel like your feelings were inconvenient. They were wrong. Your feelings are very reasonable.",
    "Your core wound: you learned very early to be useful, and now you don't know how to exist when you're not.",
    "Your core wound: at some point, love felt conditional. It probably wasn't. It probably felt that way anyway.",
    "Your core wound: you did the thing correctly and nobody noticed. You're still kind of waiting for someone to notice.",
]
if st.button("🫀 Find My Core Wound", key="wound_btn"):
    with st.spinner("gently excavating..."):
        time.sleep(1.2)
    st.info(f"💙 {random.choice(CORE_WOUNDS)}")
    st.caption("(this is a joke feature on a dumb website. but also, you're doing okay.)")
st.markdown("---")

# ===== 74 =====
st.markdown("**— 74 —**")
st.subheader("Extremely Niche Advice Column")
st.caption("Q&A for very specific situations")
ADVICE_QA = [
    ("Q: I accidentally liked a photo from 2019 while stalking someone's Instagram. What do I do?",
     "A: Unlike immediately. Put the phone down. Leave the country if necessary. Never speak of this again. They saw it."),
    ("Q: I've been saying someone's name wrong for 2 years. Do I correct myself?",
     "A: No. You take this to the grave. You spell it correctly in writing. You die knowing."),
    ("Q: I nodded along to a story I wasn't listening to. Now I have to pretend I know what happened.",
     "A: 'That's so [them]' works for any story about anyone. Nod twice. Change subject."),
    ("Q: I've been waiting for them to text back for 3 days. Do I text again?",
     "A: You may send one follow-up. One. Casual. Then you leave it. You go live your life. You have one."),
    ("Q: I said 'you too' when the waiter said 'enjoy your meal'.",
     "A: Classic. They've heard it 400 times. It's fine. You're fine. Order dessert."),
    ("Q: I've been in a meeting for 45 minutes and I have no idea what we've decided.",
     "A: Wait until someone says 'so going forward'. That's the decision. Write it down. Act like you knew."),
]
if st.button("💌 Get Advice", key="advice_col_btn"):
    q, a = random.choice(ADVICE_QA)
    st.markdown(f"*{q}*")
    st.info(a)
st.markdown("---")

# ===== 75 =====
st.markdown("**— 75 —**")
st.subheader("Speed Round: Completely Useless Trivia")
st.caption("knowledge you will deploy at exactly the wrong moment")
TRIVIA = [
    ("The shortest war in history lasted how long?", "38–45 minutes. Anglo-Zanzibar War, 1896. Someone had a very productive morning."),
    ("What is the longest word you can type with only the top row of a keyboard?", "'Typewriter'. Which is a bit on the nose."),
    ("How many times does a hummingbird flap its wings per second?", "About 50–80 times. It does not know this and doesn't care."),
    ("What is the fear of long words called?", "Hippopotomonstrosesquippedaliophobia. Someone made a choice."),
    ("What animal has rectangular pupils?", "Goats. Also some octopuses. The world is strange."),
    ("The dot over a lowercase i has a name. What is it?", "A tittle. Yes, really. Tittle."),
    ("What percentage of the ocean is unexplored?", "About 80%. There is so much down there. This should concern you more than it does."),
    ("How many hearts does an octopus have?", "Three. Two pump blood to the gills. One pumps it to the rest. Overachiever."),
]
if st.button("⚡ Speed Trivia", key="trivia_btn"):
    q, a = random.choice(TRIVIA)
    st.markdown(f"**Q:** {q}")
    with st.spinner("thinking..."):
        time.sleep(1.5)
    st.success(f"**A:** {a}")
st.markdown("---")

# ===== 76 =====
st.markdown("**— 76 —**")
st.subheader("Describe Yourself Using Only Stock Photo Keywords")
st.caption("the algorithm sees you")
STOCK_KEYWORDS = [
    "Diverse team. Casual Friday. Pointing at whiteboard. Genuine laughter. Natural light.",
    "Candid outdoor portrait. Autumnal tones. Looking into distance. Contemplative expression. Soft focus.",
    "Business casual. Confident stance. Relatable struggle. Laptop on lap. Coffee present.",
    "Millennial burnout. Urban background. Muted palette. Slightly overwhelmed. Still hustling.",
    "Cozy interior. Oversized sweater. Hot beverage. Doing fine actually. Stock photo happy.",
    "Remote worker. Kitchen table. Second monitor. Technically working. Dog somewhere nearby.",
    "Young professional. Ambitious gaze. Commuting. Slightly underpaid. Very determined.",
    "Weekend vibes. Golden hour. Effortless style. Doing a regular thing as if it's editorial.",
]
if st.button("📷 Generate My Stock Keywords", key="stock_btn"):
    st.success(f"🏷️ {random.choice(STOCK_KEYWORDS)}")
st.markdown("---")

# ===== 77 =====
st.markdown("**— 77 —**")
st.subheader("Guess the Vibe from the Playlist Title")
st.caption("music says everything")
PLAYLIST_VIBES = [
    ("'songs for driving at night'", "You're processing something. You don't want to talk about it. The road knows."),
    ("'main character'", "You've committed to a narrative arc. The arc is your commute."),
    ("'studying' (you're not studying)", "You're sitting near a textbook. The textbook is closed. The playlist is open."),
    ("'for when I'm sad but like, cozy sad'", "You have made a distinction that therapists respect."),
    ("'songs to clean to'", "High energy avoidance. The apartment gets clean. The problem does not."),
    ("'idk'", "You know. You're not ready to name it."),
    ("'2014'", "You were going through something in 2014. You are still going through it."),
    ("'villain arc'", "You've been wronged. You're composing yourself. You are preparing."),
    ("'soft'", "Extremely emotionally available today. Handle with care."),
    ("'gym' (you haven't gone to the gym)", "Aspirational. The playlist is ready. The shoes are ready. You are on the couch."),
]
if st.button("🎵 Read the Playlist Vibe", key="playlist_btn"):
    title, vibe = random.choice(PLAYLIST_VIBES)
    st.markdown(f"**Playlist:** *{title}*")
    st.info(f"**Vibe:** {vibe}")
st.markdown("---")

# ===== 78 =====
st.markdown("**— 78 —**")
st.subheader("Discontinued Product Memorial")
st.caption("gone but not forgotten")
PRODUCTS = [
    "🕯️ In memoriam: Vine. 2012-2017. Six seconds of culture. Gone too soon. The wound remains.",
    "🕯️ In memoriam: Google Reader. 2005-2013. It organized the internet. The internet did not deserve it.",
    "🕯️ In memoriam: The headphone jack on iPhones. 2007-2016. Simple. Reliable. Wired. Free.",
    "🕯️ In memoriam: Blockbuster Video. 1985-2013. One location remains in Bend, Oregon. A monument. A warning.",
    "🕯️ In memoriam: The physical keyboard on phones. Satisfying. Tactile. Missed by everyone who had one.",
    "🕯️ In memoriam: MSN Messenger. You set an away message for someone specific. They knew. You knew.",
    "🕯️ In memoriam: Flash Games. Hundreds of thousands of tiny unhinged masterpieces. Archived. Remembered. Mourned.",
    "🕯️ In memoriam: The 'poke' on Facebook. Unexplained. Unregulated. Somehow important. Discontinued. For the best.",
]
if st.button("🕯️ Pay Respects", key="memorial_btn"):
    st.info(random.choice(PRODUCTS))
st.markdown("---")

# ===== 79 =====
st.markdown("**— 79 —**")
st.subheader("The Most Unhinged Things a GPS Has Ever Said")
st.caption("turn left into the void")
GPS_LINES = [
    "In 500 feet, turn left. No. Other left. That was wrong. Recalculating.",
    "You have arrived. You have not arrived. The building is a parking lot. Recalculating.",
    "Turn right onto [street name it mispronounces with conviction for 3 years].",
    "Stay on this road for 40 miles. You have 38 miles. You have 37. You will be here a while.",
    "Take the ferry. There is no ferry. Recalculating. Take the ferry.",
    "Your destination is on the left. Your destination is a field. Recalculating.",
    "You have reached your destination. This is not your destination. Goodbye.",
    "Make a U-turn. Make a U-turn. Make a U-turn. It's fine. Continue straight. I changed my mind.",
]
if st.button("🗺️ What Did the GPS Say", key="gps_btn"):
    st.warning(f"🚗 {random.choice(GPS_LINES)}")
st.markdown("---")

# ===== 80 =====
st.markdown("**— 80 —**")
st.subheader("Powerpoint Slide Title Generator")
st.caption("for slides that contain nothing")
SLIDE_TITLES = [
    "Next Steps and Action Items (TBD)",
    "Key Takeaways (See Previous Slide)",
    "The Path Forward: A Framework for a Framework",
    "Q3 Learnings and Q4 Opportunities (Redacted)",
    "Alignment Check: Are We Aligned? (Slide 12 of 47)",
    "Thank You! Questions? (Please No Questions)",
    "Summary: What We Said in the Last 14 Slides",
    "Appendix A: Data We Collected but Won't Discuss",
    "Our Mission and Vision (Same as Last Year)",
    "Why This Matters: A High-Level Overview of Why This Matters",
]
if st.button("📊 Generate Slide Title", key="slide_btn"):
    title = random.choice(SLIDE_TITLES)
    st.success(f"📊 **Slide Title:** {title}")
    st.caption("estimated reading time: 2 seconds. estimated discussion time: 40 minutes.")
st.markdown("---")

# ===== 81 =====
st.markdown("**— 81 —**")
st.subheader("The Feelings Word Finder")
st.caption("more specific than 'fine'")
FEELINGS = [
    ("Antevasin", "Living on the border — not quite in your old life, not yet in the new one."),
    ("Limerence", "That involuntary obsessive attachment to someone. You know the one."),
    ("Sonder", "The realization that every passerby has a life as vivid and complex as your own."),
    ("Vellichor", "The strange wistfulness of a used bookstore."),
    ("Kenopsia", "The eerie feeling of a place that's usually full of people but is now empty."),
    ("Monachopsis", "The subtle but persistent feeling of being out of place."),
    ("Exulansis", "Giving up trying to explain something because others can't relate."),
    ("Jouska", "A hypothetical conversation you compulsively rehearse in your head."),
    ("Rubatosis", "The unsettling awareness of your own heartbeat."),
    ("Onism", "The frustration of being stuck in just one body that can only be in one place at a time."),
]
if st.button("💬 Find a Feeling", key="feelings_btn"):
    word, meaning = random.choice(FEELINGS)
    st.markdown(f"### {word}")
    st.info(meaning)
    st.caption("(from The Dictionary of Obscure Sorrows — a real book that exists)")
st.markdown("---")

# ===== 82 =====
st.markdown("**— 82 —**")
st.subheader("Pitch Your Life as a Netflix Series")
st.caption("elevator pitch. one sentence.")
PITCHES = [
    "A mid-level employee discovers their entire personality is their job title. Six seasons. Cancelled after two.",
    "A person attempts to finish their to-do list. Comedy. Tragedy. Twelve episodes. The list is never finished.",
    "One human navigates fourteen open browser tabs across three separate emotional crises. Limited series.",
    "A coming-of-age story about realizing adulthood is just doing things slightly more expensively. Prestige drama.",
    "Someone keeps almost sending a text and then not sending it. Character study. Three seasons.",
    "A true crime documentary about who keeps putting things back in the wrong place in the kitchen.",
    "One woman, one inbox, one mounting sense that 'unsubscribe' does nothing. Thriller.",
    "A man learns to parallel park. The series begins in 2019. He has not yet learned.",
]
if st.button("🎬 Pitch My Life", key="pitch_btn"):
    st.success(f"📺 {random.choice(PITCHES)}")
st.markdown("---")

# ===== 83 =====
st.markdown("**— 83 —**")
st.subheader("Definitive Ranking of Ways to Waste Time")
st.caption("a tier list of procrastination methods")
WASTE_METHODS = [
    ("S tier ✨", "Napping. Restorative. Guilt-free if you commit. The gold standard."),
    ("A tier", "Reorganizing something that didn't need reorganizing. Productive-feeling. Satisfying."),
    ("B tier", "Watching something you've already seen. Low stakes. Comforting. Known outcome."),
    ("C tier", "Scrolling without intent. High volume. Low return. Familiar."),
    ("D tier", "Cleaning as avoidance. Effective cleaning. Ineffective life."),
    ("F tier 💀", "Reading the comments. Every time. You know. You do it anyway."),
]
for tier, desc in WASTE_METHODS:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"**{tier}**")
    with col2:
        st.caption(desc)
st.markdown("---")

# ===== 84 =====
st.markdown("**— 84 —**")
st.subheader("Celebrity Look-Alike Generator (But Make It an Object)")
st.caption("which household item do you most resemble energetically")
OBJECT_LOOKALIKES = [
    "You give off strong 'a lamp that's been in 4 different apartments' energy.",
    "You're very much a middle drawer that has random batteries, chargers for unknown devices, and a birthday candle.",
    "You radiate 'a comfortable couch that someone put a throw blanket on' vibes.",
    "You are a whiteboard with something still faintly visible from 2 meetings ago.",
    "Your energy matches a mug that says something slightly passive aggressive but also kind of true.",
    "You are a reliable tote bag with a minor structural concern nobody's addressed yet.",
    "Energetically, you're a sticky note that's been on the monitor so long it's become part of the monitor.",
    "You give off 'an IKEA bookshelf assembled without the instructions and it's basically fine' energy.",
]
if st.button("🪞 Find My Object Twin", key="object_btn"):
    st.info(f"🏠 {random.choice(OBJECT_LOOKALIKES)}")
st.markdown("---")

# ===== 85 =====
st.markdown("**— 85 —**")
st.subheader("Unsent Message Archive")
st.caption("things we wrote and deleted")
UNSENT = [
    "I've been thinking about what you said and I think you were wrong but I understand why you said it.",
    "Hey I know it's been a while. I hope you're doing well. [deleted. too vulnerable. sent 'hey' instead. no response.]",
    "I want to come but I'm not going to come. I'm sorry in advance.",
    "I noticed what you did and I appreciated it more than I said at the time.",
    "I don't actually think I'm fine I just say that because it's easier.",
    "You were one of the most important parts of that time and I don't think you know.",
    "I meant to apologize for this years ago and I'm sorry I didn't.",
    "The honest answer to your question is I have no idea what I'm doing.",
]
if st.button("📨 Open an Unsent Message", key="unsent_btn"):
    st.info(f"📩 *\"{random.choice(UNSENT)}\"*")
    st.caption("(this is a bit, but also write the message. some of them should be sent.)")
st.markdown("---")

# ===== 86 =====
st.markdown("**— 86 —**")
st.subheader("How Old Is Your Soul (Fake Assessment)")
st.caption("based on vibe and nothing else")
SOUL_AGES = [
    ("✨ New Soul (0-100 years)", "Everything is interesting. Chaos is exciting. You're still surprised by how things work. You'll learn."),
    ("🌿 Young Soul (100-500 years)", "Finding your way. Making choices. Some of them great. Most of them instructive."),
    ("📖 Middle Soul (500-2000 years)", "Seen some things. Have opinions. Tired in a wise way. Would rather stay in."),
    ("🌌 Old Soul (2000+ years)", "Very calm. Deeply tired. Has watched civilizations rise and fall. Unsurprised by much. Excellent at naps."),
    ("🌀 Ancient Soul (timeless)", "Beyond assessment. You've been here before. Many times. You recognize things you've never seen."),
]
if st.button("👴 Assess My Soul Age", key="soul_age_btn"):
    with st.spinner("counting the rings..."):
        time.sleep(1)
    label, desc = random.choice(SOUL_AGES)
    st.markdown(f"### {label}")
    st.info(desc)
st.markdown("---")

# ===== 87 =====
st.markdown("**— 87 —**")
st.subheader("Least Helpful Productivity Advice")
st.caption("tips that don't work, delivered confidently")
BAD_PRODUCTIVITY = [
    "Just do it! (This is the advice. That's all. Just do it. Nobody has elaborated on this in 30 years.)",
    "Wake up at 5am. If you wake up at 5am and feel terrible, you're building discipline. If you feel good, you're a morning person. Either way, problem solved.",
    "Make a to-do list. Now make a list of everything on your to-do list. Now prioritize both lists. Make a third list.",
    "Eat the frog first thing in the morning. (The frog is your least desirable task. Do not eat a frog.)",
    "Use the Pomodoro technique: 25 minutes of work, 5 minute break. Spend the 5 minutes dreading the next 25 minutes.",
    "Eliminate distractions. Remove all phones, notifications, and internet access. Now you have no tools to do your job. Perfect.",
    "Visualize yourself completing the task. Spend 40 minutes visualizing. The task remains. The visualization was vivid.",
    "Just start! Beginning is the hardest part. (Beginning is not the hardest part. Continuing is the hardest part.)",
]
if st.button("💡 Give Me Bad Advice", key="bad_prod_btn"):
    st.warning(f"⏰ {random.choice(BAD_PRODUCTIVITY)}")
st.markdown("---")

# ===== 88 =====
st.markdown("**— 88 —**")
st.subheader("What Your Walk Says About You")
st.caption("gait analysis, psychologically")
WALKS = [
    "Slightly-too-fast walk: You are perpetually 4 minutes late. You have accepted this. You walk as a form of apology.",
    "The slow amble: You have nowhere to be. Everyone else is in your way. This is their problem.",
    "Purposeful-but-no-destination walk: You look like you have a meeting. You do not have a meeting. The confidence is load-bearing.",
    "Phone-out walk: You're checking something important. The importance decreases every 15 seconds. The phone stays out.",
    "Looking-at-buildings walk: You're either a tourist or deeply in your feelings. The buildings are not helping either situation.",
    "One-headphone walk: Sociable enough to be approachable. Busy enough to avoid conversation. A perfect balance.",
    "Thinking-walk: Something has happened. You're working through it. You've walked three blocks further than you intended.",
    "Speed-variable walk: Depends on who's in front of you and whether you want to pass them or pretend you don't.",
]
if st.button("🚶 Analyze My Walk", key="walk_btn"):
    st.info(f"👟 {random.choice(WALKS)}")
st.markdown("---")

# ===== 89 =====
st.markdown("**— 89 —**")
st.subheader("The Mood Ring (Text Edition)")
st.caption("what color is your mood right now")
MOOD_COLORS = [
    ("🔵 Deep Blue", "Thoughtful. Introspective. Not sad, just somewhere far away. The ocean has this color sometimes."),
    ("🟢 Muted Green", "Calm. Grounded. Alive but not dramatically so. A Tuesday in the best possible way."),
    ("🔴 Bright Red", "Alert. Activated. Something happened or nothing happened and you're annoyed either way."),
    ("🟡 Yellow", "Genuinely okay. Surprising yourself with it. Don't question it, just be yellow."),
    ("🟣 Purple", "Creative or dramatic. Possibly both. Something is brewing. It might be excellent."),
    ("⚫ Black", "Aesthetic choice OR full shutdown mode. Could be either. The mood ring isn't sure."),
    ("🟠 Orange", "Restless. Energized but unfocused. Everything seems possible in a chaotic way."),
    ("⚪ White/Clear", "Blank. A fresh nothing. Either very zen or the system is loading. Both are valid."),
]
if st.button("💍 Check the Mood Ring", key="mood_ring_btn"):
    color, desc = random.choice(MOOD_COLORS)
    st.markdown(f"### {color}")
    st.info(desc)
st.markdown("---")

# ===== 90 =====
st.markdown("**— 90 —**")
st.subheader("Extremely Honest Product Reviews")
st.caption("what the 3-star reviews are really saying")
PRODUCT_REVIEWS = [
    "★★★☆☆ — Pillow: Does what it says. Pillow-shaped. Soft enough. I've had it 4 years. No complaints. I expect nothing from it and it delivers.",
    "★★☆☆☆ — Salad: I wanted pasta. This was the responsible choice. It was fine. It knew it was a compromise. We both knew.",
    "★★★★☆ — Headphones: Excellent. One ear stopped working 14 months in. I wear them on the good side. Adapted. Still 4 stars.",
    "★★★☆☆ — My Own Motivation: Present on some days. Absent on others. No pattern. No refunds. Would not recommend to a friend but I keep using it.",
    "★☆☆☆☆ — The instructions for assembling this: Exist. Technically. I used them as a general suggestion. The result is structurally fine.",
    "★★★★★ — Couch: My best relationship. Consistent. Supportive. Available. Never judges. I've given it 5 stars. It deserves 6.",
    "★★★☆☆ — Wi-Fi: Works until it doesn't. When it doesn't, I stand closer to the router like that helps. Sometimes it helps. 3 stars.",
]
if st.button("⭐ Read a Product Review", key="product_review_btn"):
    st.warning(f"🛒 {random.choice(PRODUCT_REVIEWS)}")
st.markdown("---")

# ===== 91 =====
st.markdown("**— 91 —**")
st.subheader("Cursed Crossword Clue")
st.caption("the answer makes perfect sense")
CROSSWORD = [
    ("That thing you do when you walk into a room and forget why (8 letters)", "THURSDAY"),
    ("Sound your phone makes at 3am for no reason (5 letters)", "CRIME"),
    ("What 'working from home' looks like (8 letters)", "EXISTING"),
    ("The face you make when someone explains something you already know (11 letters)", "NODDING_LIE"),
    ("Your relationship with the snooze button (9 letters)", "DEPENDENT"),
    ("What you say to end a call when you didn't hear what they said (6 letters)", "SOUNDS"),
    ("The tab you've had open for 3 weeks (9 letters)", "INTENTION"),
    ("What 'I'll do it tomorrow' actually means (9 letters)", "NEXT_WEEK"),
]
if st.button("✏️ Give Me a Clue", key="crossword_btn"):
    clue, answer = random.choice(CROSSWORD)
    st.markdown(f"**Clue:** {clue}")
    with st.spinner("thinking hard..."):
        time.sleep(1.5)
    st.success(f"**Answer:** {answer}")
st.markdown("---")

# ===== 92 =====
st.markdown("**— 92 —**")
st.subheader("The Honest Job Description")
st.caption("what the role actually involves")
JOB_DESCS = [
    ("Senior Email Manager",
     "Responsible for sending emails about emails. Attends meetings to discuss the emails. Sends follow-up email recapping the meeting about emails."),
    ("Junior Everything",
     "Does tasks too small for senior staff and too large for interns. Learns by doing. Receives feedback by implication. Succeeds quietly."),
    ("Head of Synergy",
     "Ensures teams that should talk to each other do talk to each other. Creates slides about the talking. Attends the meeting about the slides."),
    ("Chief Vibe Officer",
     "Maintains the general feeling that everything is fine. Adjusts the feeling as needed. Reports to nobody. Answers to everyone."),
    ("Full Stack Human",
     "Handles front-end (face, appearance, interactions), back-end (emotions, logistics), and database management (memory, trauma). Always on-call."),
]
if st.button("💼 See Job Description", key="jobdesc_btn"):
    title, desc = random.choice(JOB_DESCS)
    st.markdown(f"### {title}")
    st.info(desc)
st.markdown("---")

# ===== 93 =====
st.markdown("**— 93 —**")
st.subheader("Extremely Niche Phobia Generator")
st.caption("fears that should exist and probably do")
PHOBIAS = [
    "Scrollophobia — the fear of reaching the end of your feed and having nothing left to look at.",
    "Notifitrembia — the anxiety of the notification you haven't opened but know is there.",
    "Typoregretia — the dread of a typo discovered immediately after hitting send.",
    "Chargepanic — the existential alarm of 8% battery with no charger in sight.",
    "Silencophony — the discomfort of a group chat that has suddenly gone very quiet.",
    "Replydelay — the creeping guilt of a message unanswered for more than 3 days.",
    "Bufferpause — the specific frustration of video that freezes at a critical moment.",
    "Voicemailophobia — the refusal to listen to or leave voicemails under any circumstances.",
    "Openplanangst — the unease of being watched while eating lunch at your desk.",
    "Recalcuphobia — the panic that follows immediately after taking a wrong turn.",
]
if st.button("😱 Diagnose My Phobia", key="phobia_btn"):
    st.error(f"🔬 {random.choice(PHOBIAS)}")
st.markdown("---")

# ===== 94 =====
st.markdown("**— 94 —**")
st.subheader("The Sandwich Alignment Chart")
st.caption("the definitive taxonomy")
SANDWICHES = [
    "🥖 Hot dog — a sandwich. Two pieces of bread with filling. The bun is hinged. Still bread. Still sandwich.",
    "🌮 Taco — open-faced sandwich. The fold is structural, not definitional.",
    "🌯 Burrito — a closed sandwich. The tortilla IS the bread. This is law.",
    "🍕 Pizza — open-faced sandwich on unleavened bread with toppings. Not legally a sandwich. Morally, unclear.",
    "🥪 Pop-Tart — a dessert sandwich. Two crusts. Filling. Heat-delivered. Sandwich.",
    "🍱 Sushi roll — a sandwich from another angle. Rice replaces bread. Filling remains. Philosophical sandwich.",
    "🥐 Croissant sandwich — the most sophisticated sandwich. No debate. This is agreed upon by all.",
    "🍔 Burger — peak sandwich. The ur-sandwich. The reference point by which all sandwiches are measured.",
]
if st.button("🥪 Settle the Debate", key="sandwich_btn"):
    st.info(random.choice(SANDWICHES))
st.markdown("---")

# ===== 95 =====
st.markdown("**— 95 —**")
st.subheader("The 'Explain Your Last Text Like a Legal Document'")
st.caption("terms and conditions for casual conversation")
LEGAL_TEXTS = [
    ("'k'",
     "NOTICE OF ACKNOWLEDGMENT: The undersigned hereby acknowledges receipt of your previous communication. No further action is implied, warranted, or intended by this response. All rights reserved."),
    ("'haha'",
     "The issuance of 'haha' constitutes neither admission of amusement nor confirmation of emotional engagement. This response is provided without warranty of genuine entertainment."),
    ("'sounds good'",
     "By responding 'sounds good', the party herein does not confirm full comprehension of the proposal, agreement to the terms, or intention to follow through. This is an expression of politeness only."),
    ("'omw'",
     "Estimated time of arrival is non-binding and subject to change. 'On my way' may mean departing now, departing soon, or currently locating shoes. No legal obligation is created."),
    ("'we should hang out sometime'",
     "This constitutes an expression of goodwill and not a contractual commitment. No date, time, or location has been established. This phrase does not expire but is subject to indefinite deferral."),
]
if st.button("⚖️ Legalize My Text", key="legal_btn"):
    msg, legal = random.choice(LEGAL_TEXTS)
    st.markdown(f"**Original message:** *\"{msg}\"*")
    st.info(f"**Legal translation:** {legal}")
st.markdown("---")

# ===== 96 =====
st.markdown("**— 96 —**")
st.subheader("Seasonal Mood Report")
st.caption("what the weather is doing to people")
SEASONAL = {
    "Spring (March-May)": "Optimistic. Making plans. Buying plants. 40% chance the plants survive. Wearing one layer too few. Convinced this year is different.",
    "Summer (June-Aug)": "Hot. Doing less than planned. Blaming the heat. Eating cold things. Cancelling plans in favor of staying near the fan. No regrets.",
    "Fall (Sept-Nov)": "Cozy era activated. Buying candles. Wearing a scarf preemptively. Romanticizing everything. Listening to sad music happily.",
    "Winter (Dec-Feb)": "Hibernation mode. Early nights justified. Soup as a personality. Outdoor activities reconsidered. Main activity: being inside.",
}
current_month = datetime.date.today().month
if current_month in [3, 4, 5]:
    season = "Spring (March-May)"
elif current_month in [6, 7, 8]:
    season = "Summer (June-Aug)"
elif current_month in [9, 10, 11]:
    season = "Fall (Sept-Nov)"
else:
    season = "Winter (Dec-Feb)"
st.markdown(f"**Current season:** {season}")
st.info(SEASONAL[season])
other_season = st.selectbox("or check another season:", list(SEASONAL.keys()), key="season_select")
st.caption(SEASONAL[other_season])
st.markdown("---")

# ===== 97 =====
st.markdown("**— 97 —**")
st.subheader("Scientific Name Generator (For Everyday Things)")
st.caption("latin makes everything sound important")
SCI_NAMES = [
    ("The act of opening the fridge for the third time in 10 minutes", "*Frigidus revisitatum* — compulsive cold-box consultation behavior"),
    ("The pile of clothes that is neither clean nor dirty", "*Vestimenta ambiguus* — the liminal textile formation"),
    ("Untangling headphone cables", "*Corruptus linearis extractum* — the ritual cable restoration process"),
    ("Checking your phone immediately after putting it down", "*Deviceus re-consultum* — spontaneous technological re-engagement"),
    ("Saying 'I'm almost ready' when you haven't started", "*Preparatio simulatum* — the theatrical readiness announcement"),
    ("The face you make when you're pretending to think in a meeting", "*Consideratum performativus* — the contemplation mime"),
    ("The specific sound of bubble wrap", "*Bullarum poppitum* — the satisfying pneumatic detonation ritual"),
    ("Staying up late for no reason", "*Noctis prorogatum voluntarium* — voluntary sleep postponement with no cause"),
]
if st.button("🔬 Name My Behavior", key="sciname_btn"):
    behavior, name = random.choice(SCI_NAMES)
    st.markdown(f"**Behavior:** {behavior}")
    st.info(f"**Scientific name:** {name}")
st.markdown("---")

# ===== 98 =====
st.markdown("**— 98 —**")
st.subheader("Alternate Universe Versions of You")
st.caption("parallel yous, ranked by likelihood")
ALT_YOUS = [
    "You, but you replied to that email immediately and everything is slightly different.",
    "You, but you took that one class you dropped and now you're a marine biologist.",
    "You, but you went to bed on time for one year straight. Terrifyingly functional.",
    "You, but you said what you were actually thinking in that meeting in 2019.",
    "You, but you learned to play guitar and then stopped after three months. Wait, that one exists.",
    "You, but you live somewhere you've always wanted to live. You haven't called your family in a while.",
    "You, but you're a morning person. You don't understand the evening people anymore. It's a loss.",
    "You, but you finished all your drafts. The drafts are published. Some of them did really well.",
    "You, but you said yes to that thing you said no to. It changed everything. For better. Probably.",
    "You, but slightly more rested. That's it. That's the only difference. It matters enormously.",
]
if st.button("🌀 Find an Alternate Me", key="alt_btn"):
    st.info(f"🪞 {random.choice(ALT_YOUS)}")
st.markdown("---")

# ===== 99 =====
st.markdown("**— 99 —**")
st.subheader("Receipt for Today")
st.caption("itemized breakdown of your day")
if st.button("🧾 Print Today's Receipt", key="receipt_btn"):
    now = datetime.datetime.now()
    items = [
        ("Existing (base fee)", "$0.00"),
        ("Checking phone first thing", "$3.50"),
        (f"Coffee or equivalent ({random.choice(['hot', 'iced', 'cold brew', 'whatever was available'])})", f"${random.randint(4,7)}.{random.randint(0,9)}0"),
        (f"Meetings attended ({random.randint(1,5)})", f"-${random.randint(10,30)}.00 (energy)"),
        ("Snack (justified)", f"${random.randint(1,4)}.{random.randint(0,9)}0"),
        ("Procrastination (30-90 min)", "Complimentary"),
        ("One (1) good idea", "+$25.00 (pending)"),
        ("Saying 'sounds good' without knowing what it was", "$0.00 (will cost later)"),
        ("Being generally fine", "No charge"),
    ]
    st.markdown(f"**RECEIPT — {now.strftime('%B %d, %Y')}**")
    st.markdown("```")
    for item, price in items:
        st.markdown(f"{item:<45} {price}")
    st.markdown("---")
    st.markdown(f"TOTAL: Immeasurable\nTHANK YOU FOR YOUR CONTINUED EXISTENCE")
    st.markdown("```")
st.markdown("---")

# ===== 100 =====
st.markdown("**— 100 —**")
st.subheader("🎊 Feature #100: The Hall of Fame")
st.caption("you made it to 100. here's everyone who helped.")
if st.button("🏛️ Enter the Hall of Fame", key="halloffame_btn"):
    st.balloons()
    st.snow()
    st.success("""
🏆 DUMB STUFF HALL OF FAME 🏆

Inductees:

🥇 The Button That Does Nothing — for doing nothing, consistently, every time, without complaint.

🥇 The Clicker Game — for teaching us that meaning is assigned, not inherent.

🥇 The Bad Decision Hotline — for always picking up, even at 2am.

🥇 The Final Button (now the second-to-last button) — for escalating gracefully.

🥇 The Procrastination Stage Checker — for seeing us. Really seeing us.

🥇 You — for scrolling through 100 features on a website called Dumb Stuff.
        That's either extremely impressive or a sign that you need a snack.
        We think both.

        Thank you for being here. None of this mattered.
        All of it was worth it.
        Go drink some water.
    """)

st.markdown("---")
st.markdown(
    "<div style='text-align:center;font-family:monospace;font-size:11px;color:#bbb;letter-spacing:2px;'>"
    "© DUMB STUFF · 100 FEATURES · ALL RIGHTS RESERVED · NONE OF THIS MATTERS · GO OUTSIDE"
    "</div>",
    unsafe_allow_html=True
)
