import streamlit as st
import random
import time
import datetime

st.set_page_config(page_title="DUMB STUFF", page_icon="🗑️", layout="centered")

# Reset all session state on every page load
for key in list(st.session_state.keys()):
    del st.session_state[key]


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

# ============ FEATURES 101–150 ============

# ===== 101 =====
st.markdown("**— 101 —**")
st.subheader("Rename Everyday Tasks to Sound Heroic")
st.caption("the epic reframing")
HEROIC_TASKS = [
    ("Doing laundry", "Undertaking the Great Textile Purification Ritual"),
    ("Taking out the trash", "Vanquishing the Refuse and Restoring Order to the Realm"),
    ("Replying to emails", "Navigating the Endless Scroll of Obligations"),
    ("Making coffee", "Brewing the Sacred Morning Elixir of Consciousness"),
    ("Going to sleep", "Entering the Restorative Void Until Dawn"),
    ("Eating lunch", "Refueling the Human Vessel for Continued Operation"),
    ("Checking your phone", "Consulting the Glowing Oracle of Notifications"),
    ("Washing dishes", "Cleansing the Vessels of Sustenance"),
    ("Attending a meeting", "Enduring the Council of Unclear Outcomes"),
    ("Procrastinating", "Communing with the Ancient Art of Strategic Delay"),
]
if st.button("⚔️ Make My Task Epic", key="heroic_btn"):
    task, heroic = random.choice(HEROIC_TASKS)
    st.markdown(f"**Task:** {task}")
    st.success(f"⚔️ **Heroic Version:** {heroic}")
st.markdown("---")

# ===== 102 =====
st.markdown("**— 102 —**")
st.subheader("The Definitive Hot Take Generator")
st.caption("opinions nobody asked for, delivered with confidence")
HOT_TAKES = [
    "Cereal is a soup. The milk is the broth. This is not a debate.",
    "Silence is a completely underrated form of communication and we should use it more.",
    "The best part of any movie is the first 20 minutes before anything has gone wrong yet.",
    "Afternoon is objectively better than morning and the culture has not caught up.",
    "Reading the comments is a choice you make about yourself and your afternoon.",
    "The 'skip intro' button is one of the greatest inventions of the last 20 years.",
    "Nobody has ever needed to know the time that badly but we all look at our watches when someone asks.",
    "Background music in restaurants is too loud and everyone is pretending otherwise.",
    "The correct amount of throw pillows on a couch is 2. All additional pillows are theater.",
    "Buying something you almost didn't buy and then loving it is one of life's best feelings.",
    "The middle seat on a plane should cost less. It costs the same. This is a scam.",
    "Grocery stores should tell you which checkout line is fastest but they won't because chaos.",
]
if st.button("🌶️ Drop a Hot Take", key="hottake_btn"):
    st.warning(f"🎤 {random.choice(HOT_TAKES)}")
st.markdown("---")

# ===== 103 =====
st.markdown("**— 103 —**")
st.subheader("Name That Feeling (No English Word Exists)")
st.caption("emotions that should have names")
UNNAMED_FEELINGS = [
    ("The Pre-Sneeze Suspense", "That moment when you're 95% sure a sneeze is coming but it hasn't arrived and you can't do anything else."),
    ("Post-Nap Fog", "The 4-12 minute window after a nap where you genuinely don't know what year it is."),
    ("Phantom Notification Buzz", "Feeling your phone vibrate when it didn't. Your leg is lying to you."),
    ("The Grocery Store Freeze", "Standing in an aisle, completely blanking on what you came for, slowly pushing the cart as a cover."),
    ("The Perfectly Timed Exit", "Leaving a party or meeting at exactly the right moment. Nobody saw you go. You're already home."),
    ("Reply Paralysis", "The message has been sitting there for 4 days. It gets harder every day. The longer you wait the harder it gets."),
    ("Reread Compulsion", "Reading the same sentence 4 times because your brain left the building briefly."),
    ("The Elevator Redirect", "Pressing a floor button that's already lit. You know it's already lit. You pressed it anyway."),
    ("Ambient Background Dread", "Not anxious about anything specific. Just... aware that things exist and could go wrong. Generally."),
    ("The 3pm Slump Acceptance", "The moment you stop fighting the afternoon energy crash and just let it happen."),
]
if st.button("🧠 Name a Feeling", key="namefeel_btn"):
    name, desc = random.choice(UNNAMED_FEELINGS)
    st.markdown(f"### {name}")
    st.info(desc)
st.markdown("---")

# ===== 104 =====
st.markdown("**— 104 —**")
st.subheader("Autocorrect Hall of Shame")
st.caption("it changed the wrong word with complete confidence")
AUTOCORRECTS = [
    "Wanted to say: 'omw' — sent: 'om' — recipient now thinks you're doing yoga",
    "Wanted to say: 'duck' — sent: something else — the conversation took a turn",
    "Wanted to say: 'I'll be there in a sex' — meant: 'sec' — autocorrect knew what it was doing",
    "Wanted to say: 'I'm so tired' — sent: 'I'm so tires' — technically also true",
    "Wanted to say: 'good morning!' — sent: 'good morning!' [but in a font that implies sarcasm]",
    "Wanted to say: 'that sounds good' — sent: 'that sounds gold' — now they think you loved it",
    "Wanted to say: someone's name — sent: a completely different name — they saw it",
    "Wanted to say: 'haha yeah' — sent: 'haha yea' — autocorrect removed the extra h. it felt important.",
]
if st.button("📱 See an Autocorrect Crime", key="autocorrect_btn"):
    st.error(f"💬 {random.choice(AUTOCORRECTS)}")
st.markdown("---")

# ===== 105 =====
st.markdown("**— 105 —**")
st.subheader("Your Theme Song This Week")
st.caption("the song playing in the background of your life right now")
THEME_SONGS = [
    ("🎵 Eye of the Tiger", "Something is at stake. You've decided to try. The training montage has begun."),
    ("🎵 Clair de Lune", "You are thoughtful and a little melancholy and standing near a window."),
    ("🎵 All Star by Smash Mouth", "Chaotic. Unasked for. Surprisingly upbeat. You didn't choose this."),
    ("🎵 Requiem for a Dream theme", "Something routine has been made to feel impossibly dramatic. You are doing dishes."),
    ("🎵 Here Comes the Sun", "Things are actually okay. Genuinely. This is allowed."),
    ("🎵 dramatic silence", "The universe is pausing before your next scene. Wait for it."),
    ("🎵 Yakety Sax", "Everything is happening too fast. Nothing is going as planned. It's somehow funny."),
    ("🎵 The Final Countdown", "A deadline. Real or imaginary. The countdown has begun. You are not ready."),
    ("🎵 Weightless by Marconi Union", "Calm. Clinical calm. The kind of calm that's been scientifically designed."),
    ("🎵 Mr. Brightside", "Complicated feelings. Strong opinions. It's 2006 again somehow. It's always 2006."),
]
if st.button("🎼 Find My Theme Song", key="theme_btn"):
    song, desc = random.choice(THEME_SONGS)
    st.markdown(f"### {song}")
    st.info(desc)
st.markdown("---")

# ===== 106 =====
st.markdown("**— 106 —**")
st.subheader("The Reverse Compliment Generator")
st.caption("it's technically a compliment")
REVERSE_COMPLIMENTS = [
    "You are very easy to underestimate, which is an enormous advantage.",
    "Your standards for what counts as a problem are refreshingly low.",
    "You have managed to seem like a completely normal person to most people.",
    "You're the kind of person nobody thinks to blame first.",
    "Your ability to seem like you're listening is genuinely impressive.",
    "You're consistently fine in situations that don't require more than fine.",
    "Most people tolerate you without any visible effort.",
    "You radiate a comforting sense of low-stakes involvement.",
    "Your mistakes are rarely catastrophic. That's a real skill.",
    "You make average look very achievable.",
]
if st.button("😶 Reverse Compliment Me", key="revcomp_btn"):
    st.success(f"✨ {random.choice(REVERSE_COMPLIMENTS)}")
st.markdown("---")

# ===== 107 =====
st.markdown("**— 107 —**")
st.subheader("The Time Capsule Message")
st.caption("a note to you in 10 years")
TIME_CAPSULE = [
    "Dear future you: the thing you're worried about right now either resolved itself or you stopped caring. Either way, you're fine.",
    "Dear future you: the embarrassing thing you did that you still think about? Nobody else remembers. They moved on in 48 hours.",
    "Dear future you: the years between now and then will go faster than you think. Do the thing. Take the photo. Send the message.",
    "Dear future you: you figured it out. You always do. It never feels like you will, but you do.",
    "Dear future you: at least one thing you're dreading right now turns out to be genuinely fine.",
    "Dear future you: the version of you right now is doing better than they think.",
    "Dear future you: the people who matter stayed. The ones who didn't were preparing you for the ones who did.",
    "Dear future you: you are reading this on a website called Dumb Stuff. Some things never change.",
]
if st.button("📬 Open Time Capsule", key="capsule_btn"):
    with st.spinner("opening..."):
        time.sleep(1)
    st.info(f"📜 {random.choice(TIME_CAPSULE)}")
st.markdown("---")

# ===== 108 =====
st.markdown("**— 108 —**")
st.subheader("The 'As a Child vs Now' Comparison")
st.caption("how things have changed")
CHILD_VS_NOW = [
    ("Staying up past 10pm", "AS A CHILD: forbidden, thrilling, rebellious\nNOW: accidental, regrettable, will pay for it tomorrow"),
    ("Naps", "AS A CHILD: punishment\nNOW: reward, luxury, scheduled PTO"),
    ("Getting mail", "AS A CHILD: exciting (birthday cards!!)\nNOW: threatening (bills, mostly bills)"),
    ("Fridays", "AS A CHILD: last day of school, pure joy\nNOW: survival confirmed, subdued relief"),
    ("Being called to the front of the room", "AS A CHILD: terror\nNOW: also terror, but now it's called 'presenting to stakeholders'"),
    ("Having plans cancelled", "AS A CHILD: devastating\nNOW: best news of the week"),
    ("The ice cream truck", "AS A CHILD: magical music announcing joy\nNOW: you can buy ice cream whenever you want and somehow it's less exciting"),
    ("Being asked 'what do you want to be when you grow up'", "AS A CHILD: astronaut/vet/chef\nNOW: 'functional' is the current goal"),
]
if st.button("👦 Compare Child vs Now", key="childnow_btn"):
    topic, comparison = random.choice(CHILD_VS_NOW)
    st.markdown(f"**{topic}**")
    st.info(comparison)
st.markdown("---")

# ===== 109 =====
st.markdown("**— 109 —**")
st.subheader("Microwave Minute Mysteries")
st.caption("unanswerable questions from the kitchen")
MICROWAVE_Q = [
    "Why does 1:30 feel faster than 90 seconds even though they are the same?",
    "Why do you press 2:00 when you only need 1:45? You always press 2:00.",
    "Why does the microwave beep three times even when you're standing right there?",
    "Why is the turntable broken in a way that doesn't affect cooking but makes a sound?",
    "Why does reheated coffee taste different even at the exact same temperature?",
    "Why do you open it at 0:01 to feel something?",
    "Why is 'defrost' a mode you've never successfully used?",
    "Why does the popcorn setting never work but you press it every time?",
    "Why do you clean the microwave only after something has exploded in it?",
    "Why does every microwave in every office have the clock set to the wrong time?",
]
if st.button("📡 Pose a Microwave Mystery", key="microwave_btn"):
    st.info(f"🤔 {random.choice(MICROWAVE_Q)}")
st.markdown("---")

# ===== 110 =====
st.markdown("**— 110 —**")
st.subheader("Your Obituary (Too Early, Very Funny)")
st.caption("a celebration of your minor achievements")
OBITUARIES = [
    "Passed peacefully while waiting for a page to load. Survived by 14 open browser tabs and a half-finished cup of tea.",
    "Gone too soon, mid-scroll. Is remembered for always being about to reply to that message.",
    "Departed this world having never successfully assembled IKEA furniture on the first try. Respected.",
    "Left us quietly, having just said 'I'll do it tomorrow' for the last time. Tomorrow never came.",
    "Remembered fondly for always having a snack recommendation and being right about it.",
    "Passed away having watched the same comfort show for the fourth time. No regrets expressed.",
    "Gone, but not before correctly identifying that the meeting could have been an email.",
    "Departed peacefully, having successfully avoided every phone call this week.",
]
if st.button("📰 Write My Early Obituary", key="obit_btn"):
    st.info(f"🕯️ {random.choice(OBITUARIES)}")
st.markdown("---")

# ===== 111 =====
st.markdown("**— 111 —**")
st.subheader("The 'Make It Worse' Machine")
st.caption("every situation, escalated")
MAKE_IT_WORSE = [
    ("Bad situation: you're late", "Worse: you text 'omw' from your bed"),
    ("Bad situation: awkward silence", "Worse: you fill it with a fun fact nobody wanted"),
    ("Bad situation: wrong name", "Worse: you double down"),
    ("Bad situation: sent to wrong person", "Worse: you follow up with 'ignore that' to the same wrong person"),
    ("Bad situation: locked out of your house", "Worse: your phone is also inside"),
    ("Bad situation: fell asleep in a meeting", "Worse: you were screen-sharing"),
    ("Bad situation: forgot someone's birthday", "Worse: they remembered yours last week"),
    ("Bad situation: wrong order at a restaurant", "Worse: you ate half of it before noticing"),
    ("Bad situation: missed an important email", "Worse: you replied 'thanks!' to the follow-up without reading"),
    ("Bad situation: got someone's name wrong", "Worse: you've met them seven times"),
]
if st.button("😬 Make It Worse", key="makeworse_btn"):
    bad, worse = random.choice(MAKE_IT_WORSE)
    st.markdown(f"**{bad}**")
    st.error(f"⬇️ **{worse}**")
st.markdown("---")

# ===== 112 =====
st.markdown("**— 112 —**")
st.subheader("The Unnecessary Countdown")
st.caption("count down to something that doesn't need a countdown")
if st.button("🔢 Start Unnecessary Countdown", key="uncount_btn"):
    events_silly = [
        "you finishing reading this sentence",
        "the next time you blink",
        "this button becoming less interesting",
        "the anticlimactic end of this countdown",
    ]
    event = random.choice(events_silly)
    bar = st.progress(0)
    msg = st.empty()
    for i in range(5, 0, -1):
        msg.markdown(f"### {i}... until {event}")
        bar.progress((5-i)/5)
        time.sleep(0.8)
    bar.progress(1.0)
    msg.success(f"It happened. {event.capitalize()}. As predicted.")
st.markdown("---")

# ===== 113 =====
st.markdown("**— 113 —**")
st.subheader("Dog Thoughts Translator")
st.caption("what is the dog thinking right now")
DOG_THOUGHTS = [
    "WALK?? IS THIS A WALK?? YOU PICKED UP THE KEYS THIS IS A WALK THIS IS IT THIS IS THE BEST THING—oh you're just moving them. Still exciting though.",
    "The small human dropped food. I have retrieved it. I am a hero. I will receive no medal. I am okay with this.",
    "Someone rang the doorbell. I am the only one who heard this. I must inform everyone. Loudly. Immediately.",
    "I know you're sad. I don't know why. I am going to sit on you. This is the help I am offering.",
    "That is my spot. You are in my spot. I will stare at you until you acknowledge this.",
    "You left for 8 minutes. I thought you were gone forever. You are back. This is the greatest moment of my life. Again.",
    "There is a squirrel. I don't know what I would do if I caught it. The pursuit is the point.",
    "Bath time? No. No no no no no. I am going under the bed. You cannot reach me. I am free.",
    "You said the word. The W-O-R-K word. I know what it spells. I have learned. I am devastated.",
    "I have found a stick. It is the best stick. It is too big for the door. I will make it fit.",
]
if st.button("🐕 Translate Dog Thought", key="dog_btn"):
    st.info(f"🐾 {random.choice(DOG_THOUGHTS)}")
st.markdown("---")

# ===== 114 =====
st.markdown("**— 114 —**")
st.subheader("Cat Thoughts Translator")
st.caption("what is the cat actually thinking")
CAT_THOUGHTS = [
    "I have knocked this off the table. Not because I wanted it on the floor. Because I wanted it to not be on the table.",
    "You are sleeping. This is unacceptable. It is 4am. I have needs. The need is: attention. Now.",
    "The red dot has escaped again. I know you are responsible. I am watching you.",
    "I could sit anywhere in this house. I will sit on the specific thing you are currently using.",
    "You have been gone for 9 hours. I did not miss you. I will sit near you now. This means nothing.",
    "The food is the same food as yesterday. I do not want this food. I wanted this food yesterday. That was then.",
    "I have brought you something. It is a gift. It is dead. You're welcome.",
    "This box appeared. I must be inside it. This is not a want. This is a law.",
    "You are on a video call. This is my time now. The camera will know my name.",
    "I have been staring at the wall for 11 minutes. There is nothing on the wall. I know something you don't.",
]
if st.button("🐈 Translate Cat Thought", key="cat_btn"):
    st.info(f"🐾 {random.choice(CAT_THOUGHTS)}")
st.markdown("---")

# ===== 115 =====
st.markdown("**— 115 —**")
st.subheader("The Completely Honest Tinder Bio")
st.caption("what you'd actually write if you were honest")
TINDER_BIOS = [
    "Looking for someone to eat with who doesn't make me explain my entire personality on the first date. 5'11 (in shoes, one specific pair).",
    "Genuinely funny in the right context. Quiet in most contexts. Has strong opinions about fonts. Will not text first.",
    "My love language is quality time but also not too much quality time. I need a notice period of 48 hours. Snack-driven.",
    "Professional overthinker. Casual napper. I will answer your question with a question and it will be annoying and also insightful.",
    "Looking for someone who is also just kind of figuring it out. No performance. Some chaos. Regular snack access required.",
    "I am not on here a lot. If you match me and don't message first I will also not message first and we will both disappear. Break the cycle.",
    "My friends describe me as 'a lot but in a good way' which I think means I'm interesting but they're not sure.",
    "Will remember something small you said in passing and bring it up eight months later. This is either charming or alarming.",
]
if st.button("💘 Generate Honest Bio", key="tinder_btn"):
    st.success(f"👤 {random.choice(TINDER_BIOS)}")
st.markdown("---")

# ===== 116 =====
st.markdown("**— 116 —**")
st.subheader("Rejected Hallmark Movie Titles")
st.caption("holiday films that will never be made")
HALLMARK_TITLES = [
    "A Christmas Spreadsheet: She came back to her hometown and found love AND a reconciled quarterly budget",
    "The Holiday Inbox: Could 'per my last email' become 'per our candlelit dinner'?",
    "Love, Actually, Is Complicated and This Movie Doesn't Resolve It",
    "A Snowy Second Chance: He was her high school sweetheart. She had moved on. He had not updated his LinkedIn.",
    "The Mistletoe Merger: Two rival companies. One misplaced kiss. Fourteen HR violations.",
    "December Deliverables: She always worked through Christmas. This year, the deadline was her heart.",
    "Home for the Holidays (But She Lives Here and This Is Her Apartment)",
    "The Christmas Pivot: He said he was pivoting his career. He was not. There was no pivot. Just vibes.",
    "All I Want for Christmas Is for This to Be Resolved in 90 Minutes",
    "A Very Corporate Christmas: The team-building retreat changed everything. Compliance signed off.",
]
if st.button("🎄 Generate Hallmark Title", key="hallmark_btn"):
    st.info(f"🎬 {random.choice(HALLMARK_TITLES)}")
st.markdown("---")

# ===== 117 =====
st.markdown("**— 117 —**")
st.subheader("Extremely Unhelpful Tech Support")
st.caption("have you tried turning it off and on again")
TECH_SUPPORT = [
    "Have you tried turning it off and on again? Good. Have you tried turning yourself off and on again?",
    "The issue is between the keyboard and the chair. We cannot fix this remotely.",
    "Your computer is fine. The problem is your relationship with technology.",
    "Please clear your cache, cookies, history, hopes, and expectations.",
    "We recommend uninstalling and reinstalling your approach to this task.",
    "This is a known issue. It is also a won't-fix. Thank you for your patience.",
    "Have you updated? No? Update. Yes? Uninstall the update. Install it again.",
    "Error code 404: Your motivation was not found. Please locate and reattach.",
    "We've escalated this to Tier 2. Tier 2 is on lunch. They will return in 3-5 business days.",
    "The issue is your WiFi. It's always the WiFi. Even when it isn't the WiFi.",
]
if st.button("💻 Get Tech Support", key="techsupport_btn"):
    st.warning(f"🖥️ {random.choice(TECH_SUPPORT)}")
st.markdown("---")

# ===== 118 =====
st.markdown("**— 118 —**")
st.subheader("The Complain-O-Meter")
st.caption("rate your complaint, get context")
complaint_level = st.slider("how bad is your complaint? (1=mild, 10=catastrophic)", 1, 10, 5, key="complaint_meter")
if st.button("📊 Rate My Complaint", key="complain_rate_btn"):
    if complaint_level <= 2:
        st.info("Level 1-2: This is a minor inconvenience. A fine has been noted. No action required.")
    elif complaint_level <= 4:
        st.info("Level 3-4: A legitimate grievance. You are justified. Please complain to one (1) trusted friend and then release it.")
    elif complaint_level <= 6:
        st.warning("Level 5-6: A real problem. You may vent freely for up to 10 minutes. Then: snack, water, assess.")
    elif complaint_level <= 8:
        st.warning("Level 7-8: Significant. You deserve sympathy AND practical help. Call someone. Actually call them.")
    else:
        st.error("Level 9-10: This is serious. Please stop using this website and address the actual situation.")
st.markdown("---")

# ===== 119 =====
st.markdown("**— 119 —**")
st.subheader("Things That Sound Fake But Aren't")
st.caption("real facts that your brain refuses to accept")
SOUNDS_FAKE = [
    "Oxford University is older than the Aztec Empire. Oxford: ~1096 CE. Aztecs: ~1300 CE. The university was there first.",
    "Cleopatra lived closer to the invention of the iPhone than to the construction of the Great Pyramid.",
    "A day on Venus is longer than a year on Venus. Venus takes longer to spin than to orbit the sun.",
    "There are more possible iterations of a game of chess than atoms in the observable universe.",
    "The fax machine was invented before the telephone.",
    "Nintendo was founded in 1889. It sold playing cards. The Game Boy came 100 years later.",
    "Alaska is simultaneously the most northern, most western, AND most eastern state in the US.",
    "The woolly mammoth was still alive when the Great Pyramid was being built.",
    "A teaspoon of neutron star material weighs about 10 million tons.",
    "Sharks are older than trees. Sharks: 450 million years ago. Trees: 350 million years ago.",
]
if st.button("🤯 Tell Me Something That Sounds Fake", key="soundsfake_btn"):
    st.info(f"🧠 {random.choice(SOUNDS_FAKE)}")
st.markdown("---")

# ===== 120 =====
st.markdown("**— 120 —**")
st.subheader("2-Sentence Horror Stories (Mundane Edition)")
st.caption("the real horror is relatable")
MUNDANE_HORROR = [
    "I checked the time. It was Monday.",
    "The email sent successfully. I had replied to all.",
    "I sat down to do one quick thing. Six hours passed.",
    "I said 'you too' when the waiter said enjoy your meal. We both heard it.",
    "I opened the fridge. I had just opened it 4 minutes ago and everything was still the same.",
    "I had a great idea in the shower. By the time I dried off, it was gone.",
    "I started a new series. It was cancelled after one season.",
    "I felt my phone buzz in my pocket. I checked it. The buzz had been imaginary.",
    "I read the email. I closed the email. The email remains unresponded to. It has been 9 days.",
    "I set an alarm for 7am. I woke up at 6:58. I waited.",
]
if st.button("😱 Tell Me a Mundane Horror Story", key="horror_btn"):
    st.error(f"🕯️ {random.choice(MUNDANE_HORROR)}")
st.markdown("---")

# ===== 121 =====
st.markdown("**— 121 —**")
st.subheader("What Your Handwriting Says About You")
st.caption("graphology, but made up")
HANDWRITING = [
    ("Large letters", "You take up space confidently. Or you ran out of room at the bottom. One of those."),
    ("Tiny letters", "Detail-oriented. Private. Or you were trying to fit a lot on one page. Efficient either way."),
    ("Messy handwriting", "Your brain moves faster than your hand. Ideas first, legibility later. Smart people signature."),
    ("Very neat handwriting", "You were praised for this as a child and it stuck. The neatness is load-bearing."),
    ("All caps", "You mean business. You also possibly learned to write from a very authoritative source."),
    ("Letters slanting right", "Optimistic. Forward-leaning. Excited about what's coming."),
    ("Letters slanting left", "Reflective. Private. Looking back more than forward. Probably fine."),
    ("Mix of print and cursive", "Chaotic neutral. Makes decisions mid-sentence and doesn't go back."),
    ("Can't read your own handwriting", "You write as a performance of writing, not to communicate. The notes are decorative."),
]
if st.button("✍️ Analyze My Handwriting", key="handwriting_btn"):
    style, analysis = random.choice(HANDWRITING)
    st.markdown(f"**Style:** {style}")
    st.info(analysis)
st.markdown("---")

# ===== 122 =====
st.markdown("**— 122 —**")
st.subheader("The 'Describe Your Personality as Weather' Button")
st.caption("meteorological self-assessment")
PERSONALITY_WEATHER = [
    "You're partly cloudy with a chance of overthinking. Mostly harmless. Occasional brief sunshine.",
    "You're a sudden thunderstorm — calm beforehand, intense during, clear after. People are rarely prepared.",
    "You're dense morning fog. Hard to read at first. Burns off slowly. Once you do, visibility is excellent.",
    "You're a comfortable 72°F with no humidity and a light breeze. People stay longer than they planned.",
    "You're a week-long drizzle. Present, consistent, slightly melancholic, weirdly cozy.",
    "You're a surprise heat wave in October. Unexpected. Delightful. Shouldn't be this warm but somehow is.",
    "You're clear skies after a week of rain. Earned. Appreciated. Makes everything look better.",
    "You're that specific kind of grey sky that isn't gloomy, it's just... thinking.",
    "You're a warm front moving in. People around you feel better without knowing why.",
    "You're a perfectly timed breeze on a hot day. Underappreciated until you show up.",
]
if st.button("🌤️ What Weather Am I?", key="weather_pers_btn"):
    st.info(f"🌡️ {random.choice(PERSONALITY_WEATHER)}")
st.markdown("---")

# ===== 123 =====
st.markdown("**— 123 —**")
st.subheader("Press Conference Simulator")
st.caption("answer the impossible question")
PRESS_QUESTIONS = [
    "Following today's nap, what can you tell us about your plans for the rest of the afternoon?",
    "Reports suggest you opened the fridge four times in the last hour. What were you looking for?",
    "Can you confirm or deny that you sent that text and then immediately regretted it?",
    "At what point did you decide the meeting was over for you personally, while still physically present?",
    "Our sources indicate you haven't replied to that message. Is there a statement you'd like to make?",
    "How do you respond to allegations that you started a new show knowing full well you wouldn't finish it?",
    "You've been described as 'fine'. Do you stand by that assessment?",
    "Can you walk us through the decision to go to bed at 10pm and then be awake at 2am for no reason?",
]
if st.button("🎤 Face the Press", key="press_btn"):
    q = random.choice(PRESS_QUESTIONS)
    st.markdown(f"**REPORTER:** {q}")
    responses = [
        "I have no comment at this time.",
        "We will be releasing a full statement via text to one (1) trusted friend.",
        "I'd like to redirect to what I feel are the more important issues.",
        "That question contains several assumptions I'm not prepared to address.",
        "I think what's really important here is that we move forward.",
        "No further questions.",
    ]
    st.info(f"**YOUR RESPONSE:** *{random.choice(responses)}*")
st.markdown("---")

# ===== 124 =====
st.markdown("**— 124 —**")
st.subheader("The Overthinking Spiral Simulator")
st.caption("one thought, many directions")
SPIRALS = [
    "They said 'sounds good' → but usually they say 'great' → did I do something → the last message was fine → maybe they're busy → they're definitely annoyed → I'm overthinking → but what if I'm not → sounds good.",
    "I didn't hear what they said → I nodded anyway → what if they asked a question → what if they're waiting for an answer → I'll just nod again → if they ask I'll say 'yeah absolutely' → what does 'yeah absolutely' mean in context → unclear.",
    "The email took 3 days to reply → that's a lot → usually faster → something happened → or they're just busy → everyone's busy → it's fine → what did I send in the last email → rereading the last email → the last email is fine → why did it take 3 days.",
    "They laughed at my joke → but was it a real laugh → it sounded real → or polite → polite laughs are slightly shorter → that might have been shorter → I can't remember the length → I'll never know → the joke was fine → probably.",
]
if st.button("🌀 Start the Spiral", key="spiral_btn"):
    st.warning(f"💭 {random.choice(SPIRALS)}")
st.markdown("---")

# ===== 125 =====
st.markdown("**— 125 —**")
st.subheader("Morning Person vs Night Person Alignment Chart")
st.caption("which one are you really")
ALIGNMENT = [
    ("☀️ True Morning Person", "Up at 6. Genuinely happy about it. Has done three things before you've opened your eyes. You find them suspicious."),
    ("🌅 Reluctant Morning Person", "Up early by necessity. Functional by 8:30. Don't speak to them before coffee. They know."),
    ("😶 Neither Person", "Awake at times. Tired at times. No pattern. Not aligned with any cosmic schedule. A mystery."),
    ("🌆 Afternoon Person", "Peak performance: 2-6pm. Underrepresented in the schedule conversation. Valid."),
    ("🌙 True Night Person", "Alive after 10pm. Thinking clearest at midnight. Has solved problems at 2am that daylight couldn't crack."),
    ("🕯️ Chaotic Schedule Person", "Asleep at random. Awake at random. The body has suggestions. They are being ignored. Functioning somehow."),
]
if st.button("⏰ Find My Time Alignment", key="timealign_btn"):
    label, desc = random.choice(ALIGNMENT)
    st.markdown(f"### {label}")
    st.info(desc)
st.markdown("---")

# ===== 126 =====
st.markdown("**— 126 —**")
st.subheader("The Menu Item You'd Order at a Restaurant Called 'Your Life'")
st.caption("a personal dining experience")
LIFE_MENU = [
    "The Daily Special: Whatever You Were Supposed to Do Today, Warmed Over — served with a side of 'still counts'",
    "The Comfort Bowl: Familiar content, familiar snacks, familiar worries — no substitutions",
    "The Ambitious Tasting Menu: 12 courses, 3 actually consumed, the rest left for tomorrow — market price",
    "The Working Lunch: Eaten at desk, forgotten immediately, definitely had something in it — $14",
    "The Late Dinner: Started too late, finished too late, completely worth it — no regrets",
    "The Brunch (served all day): Neither fully breakfast nor lunch, existing in a liminal space — mimosa optional",
    "The 'I'll Just Have Something Small': Escalated significantly. Not small. No notes.",
    "The Leftovers: Surprisingly good second time around. Some things get better.",
]
if st.button("🍽️ See My Menu Item", key="lifemenu_btn"):
    st.info(f"🍴 {random.choice(LIFE_MENU)}")
st.markdown("---")

# ===== 127 =====
st.markdown("**— 127 —**")
st.subheader("Extremely Specific Hobbies That Should Exist")
st.caption("niche interests for the modern era")
HOBBIES = [
    "Competitive Fridge Reorganization — timed events, judged on efficiency and aesthetic",
    "Ambient Sound Identification — naming the exact HVAC hum in any building within 30 seconds",
    "Aggressive Normcore Fashion — looking as average as possible, on purpose, with effort",
    "Recreational Overthinking — structured, timed, with a formal debrief",
    "Extreme Coupon Stacking for Things You Don't Need — Olympic category pending",
    "Speed Autobiography Writing — your whole life story, 500 words, 10 minutes, go",
    "Competitive Napping — scored on depth, duration, and post-nap clarity",
    "Artisanal Procrastination — doing nothing, but intentionally and with craft",
    "Retroactive Calendar Planning — scheduling things after they've happened to feel organized",
    "Amateur Furniture Tetris — fitting items into spaces they shouldn't fit in",
]
if st.button("🎯 Find My Hobby", key="hobby_btn"):
    st.success(f"🏅 {random.choice(HOBBIES)}")
st.markdown("---")

# ===== 128 =====
st.markdown("**— 128 —**")
st.subheader("The Universal Translator for 'Fine'")
st.caption("'fine' means many things")
FINE_TRANSLATIONS = [
    ("Fine (single word, period)", "Not fine. Deeply not fine. The period is doing heavy work here."),
    ("Fine! (exclamation point)", "Resigned. This has been agreed to under protest. Do not celebrate."),
    ("Fine... (ellipsis)", "Something is being left unsaid. It is significant. Ask once. Only once."),
    ("I'm fine (unprompted)", "You did not ask. They told you anyway. Something happened."),
    ("It's fine (about someone else's thing)", "It is not fine with them. They are being diplomatic."),
    ("Fine, FINE (repeated)", "The first fine was a lie. The second fine is an admission."),
    ("That's fine (about your thing)", "They have accepted this. They have opinions about it. They will not share them now."),
    ("I said I'm fine", "You asked more than once. The case is closed. Do not reopen the case."),
]
if st.button("🔍 Translate 'Fine'", key="fine_btn"):
    version, meaning = random.choice(FINE_TRANSLATIONS)
    st.markdown(f"**They said:** *\"{version}\"*")
    st.info(f"**They meant:** {meaning}")
st.markdown("---")

# ===== 129 =====
st.markdown("**— 129 —**")
st.subheader("The Unhinged Life Coach")
st.caption("motivation from the abyss")
LIFE_COACH = [
    "Your comfort zone is a lie you've built with soft furnishings and familiarity. Rearrange one piece of furniture today. That's growth.",
    "The version of you that 'has it together' is three naps and a stable sleep schedule away. You're not far.",
    "Stop waiting for the right time. There is no right time. There is only now and the snack you should have gotten before sitting down.",
    "You are the CEO of your own life. The CFO, the intern, and the IT department who takes 3 days to respond. All of them.",
    "What would you do if you weren't afraid? Do that. Or think about doing it. Both count for now.",
    "The journey of a thousand miles begins with a single step. You haven't taken the step. Take the step. Or tomorrow. But take the step.",
    "Success is rented, not owned. The rent is paid daily. The rent is manageable. You can afford the rent.",
    "You are exactly where you're supposed to be. Unless you're supposed to be somewhere else. Check your calendar.",
]
if st.button("💪 Get Coached", key="coach_btn"):
    with st.spinner("channeling the energy..."):
        time.sleep(0.8)
    st.success(f"🦁 {random.choice(LIFE_COACH)}")
st.markdown("---")

# ===== 130 =====
st.markdown("**— 130 —**")
st.subheader("The 'What Decade Are You Stuck In' Quiz")
st.caption("your soul's hometown")
DECADES = [
    ("📼 The 80s", "You believe in shoulder pads, synth music, and the possibility that things will work out through sheer effort and montage."),
    ("💿 The 90s", "Flannel. Dial-up. The vague sense that everything is ironic but also sincere. Slurpees."),
    ("📀 The 2000s", "You still have opinions about Myspace. Low-rise jeans traumatized you. The ringtone era shaped you."),
    ("📱 The 2010s", "Instagram aesthetic. Artisanal everything. The word 'hustle' before you were tired of it."),
    ("🌐 The 2020s", "You were there. You are still there. You don't fully know what's happening but you're present for it."),
    ("📺 The 70s", "Warm. Analog. Suspicious of efficiency. Believes in slow things and longer stories."),
    ("🎵 The 60s", "Idealistic. Confused. Something is definitely changing. Not sure if that's good yet."),
]
if st.button("📅 Find My Decade", key="decade_btn"):
    label, desc = random.choice(DECADES)
    st.markdown(f"### {label}")
    st.info(desc)
st.markdown("---")

# ===== 131 =====
st.markdown("**— 131 —**")
st.subheader("Plausible Lies You Could Tell at a Party")
st.caption("conversational options")
PARTY_LIES = [
    "I was briefly a professional chess player. (You played as a child. You were not professional.)",
    "I know a surprisingly large amount about the history of fonts. (Actually true for many people. Use with caution.)",
    "I've been to every state except one. (Pick one you've never mentioned to this person.)",
    "I'm training for something. (Unspecified. Leave it vague. They'll fill in the gaps.)",
    "I was on a TV show once. Briefly. In the background. (Technically possible for many people.)",
    "I used to be really into competitive something. (Anything. Badminton. Trivia. Folding.)",
    "I know the person who invented [thing]. (Pick an obscure thing. Nobody will fact-check.)",
    "I briefly lived abroad. (Duration undefined. Country unspecified. Vibes only.)",
]
if st.button("🎭 Give Me a Party Lie", key="partylie_btn"):
    st.warning(f"🤥 {random.choice(PARTY_LIES)}")
    st.caption("(we are not responsible for the consequences)")
st.markdown("---")

# ===== 132 =====
st.markdown("**— 132 —**")
st.subheader("Fake Band Genres")
st.caption("music categories that don't exist but should")
FAKE_GENRES = [
    "Post-Ironic Ambient Folk — sounds like a hiking playlist but the lyrics are about spreadsheets",
    "Aggressive Cozy Core — intense bedroom pop for people who are furious about being comfortable",
    "Corporate Noir Jazz — Miles Davis if he worked in procurement",
    "Sad Banger — technically a banger. emotionally a funeral. you're dancing but you're not okay",
    "3AM Indie — only listenable between 2-4am. loses all power in daylight",
    "Reluctant Hyperpop — they didn't mean to make this. they're as surprised as you are.",
    "Commuter Metal — aggressive enough to handle rush hour. no louder.",
    "Melancholy Lounge — smooth, quiet, you ordered the wrong thing but you're not sending it back",
    "Emotional Infrastructure — music that feels like a building. stable. slightly cold. important.",
    "Nostalgia-Adjacent Pop — sounds like something you remember but isn't from anything real",
]
if st.button("🎸 Name a Fake Genre", key="genre_btn"):
    st.success(f"🎵 {random.choice(FAKE_GENRES)}")
st.markdown("---")

# ===== 133 =====
st.markdown("**— 133 —**")
st.subheader("Today's Affirmation (Realistic Edition)")
st.caption("affirmations that meet you where you are")
AFFIRMATIONS = [
    "I am doing an acceptable amount given the circumstances.",
    "My best today is what I have today, and today I have slightly less than yesterday, and that's allowed.",
    "I am a work in progress. The work is progressing at a reasonable pace. Not fast. Not stopped.",
    "I deserve rest even when I haven't earned it by any objective measure.",
    "I am more than my productivity, although I don't fully believe that yet and that's okay too.",
    "My feelings are valid, even the ones that don't make sense and the ones I'm embarrassed about.",
    "Things have been hard. Not every day, but some of them. I'm still here.",
    "I am allowed to be uncertain. I am allowed to not know. I am allowed to be in the middle of figuring it out.",
    "I don't have to be inspiring today. I can just be here.",
    "I have survived every hard day so far. The odds are currently in my favor.",
]
if st.button("🌱 Give Me an Affirmation", key="affirm_btn"):
    st.info(f"💚 {random.choice(AFFIRMATIONS)}")
st.markdown("---")

# ===== 134 =====
st.markdown("**— 134 —**")
st.subheader("The Unnecessary Product Comparison")
st.caption("pitting two things against each other that have never competed")
COMPARISONS = [
    ("Pencils vs Pens", "Pencils: erasable, forgiving, humble. Pens: committed, permanent, confident. Choose your personality."),
    ("Stairs vs Elevator", "Stairs: effort, virtue, sometimes faster. Elevator: surrender, efficiency, also sometimes faster. No wrong answer."),
    ("Morning shower vs Evening shower", "Morning: functional, prepares. Evening: earned, decompress. Both are correct. Neither is wrong. This debate has no stakes."),
    ("Headphones vs Earbuds", "Headphones: commitment, isolation, a statement. Earbuds: portable, casual, one will stop working in 14 months."),
    ("Texting vs Calling", "Texting: asynchronous, documented, controllable. Calling: real-time, terrifying, occasionally necessary."),
    ("Sticky notes vs To-do apps", "Sticky notes: tangible, satisfying, covered in your handwriting. Apps: synced, searchable, and you'll stop checking them by Thursday."),
]
if st.button("⚖️ Compare Two Things", key="compare_btn"):
    item1_vs_item2, analysis = random.choice(COMPARISONS)
    st.markdown(f"**{item1_vs_item2}**")
    st.info(analysis)
st.markdown("---")

# ===== 135 =====
st.markdown("**— 135 —**")
st.subheader("The Suspiciously Specific Horoscope")
st.caption("the stars know too much")
SPECIFIC_HOROSCOPES = [
    "Mercury entering your third house means the email you've been avoiding will gain a follow-up tomorrow. You already know which one.",
    "Venus in retrograde suggests someone will say 'let's catch up soon' to you this week. Neither of you will follow up. The stars do not judge.",
    "Mars is in a challenging aspect with your snack drawer. The snack you want is not there. There is a granola bar. You don't want the granola bar.",
    "The moon is in the phase where you check your phone, find nothing interesting, put it down, and check it again within 45 seconds.",
    "Jupiter's position indicates that today you will start doing something, pause to look something up, and forget what you were originally doing.",
    "Saturn return energy suggests the next thing you open will take longer to load than you expected.",
    "Neptune in your sector of sleep patterns means you'll be tired at 9pm, awake at 11pm for no reason, and tired again at 2am.",
    "The alignment of the outer planets suggests that someone will ask 'how are you' and you will say 'good, you?' before processing the question.",
]
if st.button("⭐ Read My Specific Horoscope", key="spechoro_btn"):
    st.warning(f"🔮 {random.choice(SPECIFIC_HOROSCOPES)}")
st.markdown("---")

# ===== 136 =====
st.markdown("**— 136 —**")
st.subheader("The 'Explain It Like I'm 5' But Make It Philosophical")
st.caption("simple language, big questions")
ELI5_PHILOSOPHY = [
    ("Why do we exist?", "Nobody knows! And that's okay. You exist right now and that's already kind of wild, right?"),
    ("What is time?", "Imagine a river but you can't see it and you can only stand in it and you can't go upstream. That's time."),
    ("What happens when we die?", "Most scientists think it's like before you were born. You weren't sad then. So probably fine."),
    ("What is love?", "It's when you really really like someone being around and you want good things for them even when you're not there."),
    ("What is consciousness?", "It's the weird feeling of being you and knowing you're you. Nobody knows why it happens. Even the smartest people."),
    ("Is any of this real?", "Probably! And even if it isn't, it feels real, so it kind of counts anyway."),
    ("Why do bad things happen?", "Because the universe doesn't have feelings and things just happen. But the good news is: people do have feelings. That's us. We help."),
    ("What is the meaning of life?", "We don't think there's a built-in one. Which means you get to pick yours. That's a lot of freedom. It can feel like pressure. It's actually a gift."),
]
if st.button("🧒 Explain Something Big Simply", key="eli5_btn"):
    q, a = random.choice(ELI5_PHILOSOPHY)
    st.markdown(f"**Question:** {q}")
    st.info(f"**Simple answer:** {a}")
st.markdown("---")

# ===== 137 =====
st.markdown("**— 137 —**")
st.subheader("The Honest Weather Forecast")
st.caption("what the weather actually means for your plans")
HONEST_FORECASTS = [
    "☀️ Sunny and 75°F: Perfect. You won't go outside. You'll see it through a window and feel vaguely good about it.",
    "🌧️ Rainy all day: All plans have been internally cancelled. Cozy mode activated without negotiation.",
    "⛅ Partly cloudy: A meaningless forecast. Could be anything. Bring a layer. Don't bring a layer. Unknown.",
    "🌨️ Light snow: Beautiful for 40 minutes. Then a commute problem. Then a dirty slush problem. Then a memory.",
    "🌬️ Windy: Your umbrella will turn inside out. This will happen at the worst moment. You know this.",
    "🌫️ Foggy: Eerie. Cinematic. You'll take a photo. It won't capture it. You'll know you were there.",
    "🌡️ Heat advisory: Do nothing. Stay still. The heat is the event. You are surviving it. That counts.",
    "⛈️ Thunderstorm: Dramatic. Nature is having a moment. Stay inside. Watch it. Have a hot drink. Correct behavior.",
]
if st.button("🌤️ Get Honest Forecast", key="forecast_btn"):
    st.info(random.choice(HONEST_FORECASTS))
st.markdown("---")

# ===== 138 =====
st.markdown("**— 138 —**")
st.subheader("Discontinued Slang Translator")
st.caption("words that used to mean things")
OLD_SLANG = [
    ("'Groovy'", "Modern equivalent: 'vibe'. Same energy. Different decade. Still correct."),
    ("'Radical'", "Modern equivalent: 'fire' or 'absolutely unhinged (complimentary)'."),
    ("'Gnarly'", "Modern equivalent: 'actually insane' or 'no thoughts, just chaos'. High praise."),
    ("'Far out'", "Modern equivalent: 'okay but like... what?' in a positive, surprised way."),
    ("'The bee's knees'", "Modern equivalent: 'it's literally everything'. Bees' knees remain relevant."),
    ("'Hip'", "Modern equivalent: 'very much a thing right now'. The word 'hip' is no longer hip."),
    ("'Nifty'", "Modern equivalent: 'lowkey kind of genius'. Underused. Should return."),
    ("'Catch you on the flip side'", "Modern equivalent: 'ok bye' with slightly more drama and optimism."),
]
if st.button("📖 Translate Old Slang", key="slang_btn"):
    word, translation = random.choice(OLD_SLANG)
    st.markdown(f"**Word:** {word}")
    st.info(f"**Translation:** {translation}")
st.markdown("---")

# ===== 139 =====
st.markdown("**— 139 —**")
st.subheader("Tiny Victories Board")
st.caption("celebrating the small wins")
TINY_VICTORIES = [
    "🏆 You woke up before your alarm. The alarm was unnecessary. You beat it.",
    "🏆 You remembered to charge your phone before it hit 10%. A rare success.",
    "🏆 You found parking on the first try. The universe cooperated.",
    "🏆 You finished a chapstick. All the way. The whole thing. Without losing it.",
    "🏆 You sent a difficult message and it went fine.",
    "🏆 You fell asleep fast last night. No lying awake. Just: sleep. Incredible.",
    "🏆 You ate a vegetable today without it being the whole personality of the meal.",
    "🏆 You remembered a name you thought you'd forgotten.",
    "🏆 You said no to something and it was fine and nothing bad happened.",
    "🏆 You made your bed. On a weekday. Without anyone asking.",
    "🏆 You responded to something the same day. Not the next day. The same day.",
    "🏆 You found the thing you lost in the last place you looked. As always. But still.",
]
if st.button("🎉 Celebrate a Tiny Victory", key="victory_btn"):
    st.success(random.choice(TINY_VICTORIES))
st.markdown("---")

# ===== 140 =====
st.markdown("**— 140 —**")
st.subheader("The 'What if Everything Was Fine' Scenario")
st.caption("radical optimism, one button at a time")
EVERYTHING_FINE = [
    "What if the thing you're dreading just... goes fine? Like, actually fine. No drama. Fine.",
    "What if you wake up tomorrow feeling rested? It has happened before. It could happen again.",
    "What if that conversation you're avoiding is actually pretty easy when you have it?",
    "What if the email you send today gets a warm, helpful response within the hour?",
    "What if you go to the thing and actually enjoy it?",
    "What if this year you finish the project?",
    "What if people like you more than you think? (They probably do.)",
    "What if the thing you've been putting off takes 15 minutes and then it's just done?",
    "What if the bad stretch you've been in is almost over?",
    "What if it works out?",
]
if st.button("🌈 What If Everything Was Fine", key="whatiffine_btn"):
    st.success(f"💚 {random.choice(EVERYTHING_FINE)}")
st.markdown("---")

# ===== 141 =====
st.markdown("**— 141 —**")
st.subheader("Vintage Error Messages")
st.caption("computer problems from a simpler time")
ERROR_MSGS = [
    "FATAL ERROR: User has attempted to do too much. System will now do nothing until further notice.",
    "WARNING: You have unsaved feelings. Would you like to save? [Yes] [No] [Ask Me Again in 3 Years]",
    "404 MOTIVATION NOT FOUND: The resource you requested has been temporarily relocated to next week.",
    "GENERAL PROTECTION FAULT in module MONDAY.EXE at 0000:07:00 — please contact IT (the IT is a nap)",
    "INSUFFICIENT MEMORY: Please close 14 of your 47 open thoughts before continuing.",
    "ILLEGAL OPERATION: User attempted to do something reasonable. This is not supported.",
    "DISK FULL: Your brain has reached maximum storage. Please delete one (1) embarrassing memory from 2009.",
    "CONNECTION TIMED OUT: The person you are trying to reach has entered Do Not Disturb mode indefinitely.",
    "KERNEL PANIC: Too many feelings loaded at startup. Safe mode activated. Couch engaged.",
    "ERROR 418: I am a teapot. This is not relevant to your situation but it is a real HTTP error code.",
]
if st.button("💾 Generate Error Message", key="error_btn"):
    st.error(f"🖥️ {random.choice(ERROR_MSGS)}")
st.markdown("---")

# ===== 142 =====
st.markdown("**— 142 —**")
st.subheader("The Honest Dating Profile for a City")
st.caption("what it's actually like to live there")
CITY_PROFILES = [
    ("New York, NY", "Loud. Fast. Expensive in ways that keep surprising you. But once it loves you back, you can't leave. Emotionally unavailable. 10/10."),
    ("Los Angeles, CA", "Warm. Sprawling. Everyone is working on something. Traffic is a personality trait here. The sunsets are absurdly good."),
    ("Chicago, IL", "Seasons with full commitment. Deep dish is a lifestyle. The lake is enormous and cold and beautiful."),
    ("Portland, OR", "Extremely good coffee. Extreme weather opinions. Something is always fermenting somewhere nearby."),
    ("Austin, TX", "Hot. Getting hotter. Used to be weird. Getting less weird. Still has the music. Still has the brisket."),
    ("Seattle, WA", "Grey sky as a default. Extraordinary nature 30 minutes in any direction. People are polite and slightly unreachable until they're not."),
    ("Nashville, TN", "More neon than expected. Bachelorette parties as a local phenomenon. The music roots run deep under the tourist layer."),
    ("Denver, CO", "Altitude will get you first. Then the outdoors will get you. Then you'll never want to leave."),
]
if st.button("🏙️ Rate a City", key="city_btn"):
    city, desc = random.choice(CITY_PROFILES)
    st.markdown(f"### 📍 {city}")
    st.info(desc)
st.markdown("---")

# ===== 143 =====
st.markdown("**— 143 —**")
st.subheader("The 'What Kind of Chaos Are You' Sorter")
st.caption("not all chaos is equal")
CHAOS_TYPES = [
    ("🌀 Organized Chaos", "You know where everything is. Nobody else does. You describe this as 'a system'."),
    ("🌪️ Sudden Chaos", "Fine for long stretches. Then everything at once. No middle ground."),
    ("🎲 Random Chaos", "Unpredictable schedule. Unpredictable choices. Consistent outcomes somehow."),
    ("🎭 Performative Chaos", "You are not as chaotic as you present. The chaos is a brand. You have a budget."),
    ("🧩 Structured Chaos", "Chaos within a framework. You have rules. The rules are just unusual."),
    ("🌊 Slow-Building Chaos", "Everything seems fine. Then it isn't. You saw it coming. You said nothing."),
    ("🪄 Productive Chaos", "You work best in a mess. The mess is the method. It produces results. Inexplicably."),
    ("🤷 Accidental Chaos", "You didn't mean to. You rarely mean to. It keeps happening. The chaos finds you."),
]
if st.button("🌪️ What Chaos Am I?", key="chaos_btn"):
    kind, desc = random.choice(CHAOS_TYPES)
    st.markdown(f"### {kind}")
    st.info(desc)
st.markdown("---")

# ===== 144 =====
st.markdown("**— 144 —**")
st.subheader("Two Truths and a Lie (About the Universe)")
st.caption("one of these is false. or maybe they all are.")
TWO_TRUTHS = [
    ("1. Cleopatra lived closer to the Moon landing than to the pyramids.\n2. A day on Venus is longer than its year.\n3. The sun makes a sound but we can't hear it in space.",
     "All three are TRUE. The universe is unhinged."),
    ("1. Bananas are slightly radioactive.\n2. Hot water freezes faster than cold water under some conditions.\n3. There are more grains of sand on Earth than stars in the observable universe.",
     "All three are TRUE. We live in a fever dream."),
    ("1. Sharks are older than trees.\n2. Fax machines were invented before telephones.\n3. Humans and T-Rex are separated by more time than T-Rex and Stegosaurus.",
     "All three are TRUE. Time is a strange shape."),
    ("1. Oxford University is older than the Aztec Empire.\n2. Mammoths were alive when the Great Pyramid was built.\n3. You are always moving through time at exactly one second per second.",
     "All three are TRUE. Chronology is wild."),
]
if st.button("🤔 Play Two Truths and a Lie", key="twotruths_btn"):
    question, reveal = random.choice(TWO_TRUTHS)
    st.markdown(question)
    with st.spinner("which one is the lie..."):
        time.sleep(2)
    st.success(f"**Reveal:** {reveal}")
st.markdown("---")

# ===== 145 =====
st.markdown("**— 145 —**")
st.subheader("Background Character Energy Levels")
st.caption("how much of a side character are you right now")
BACKGROUND_LEVELS = [
    ("🧍 Level 1: Ambient Human", "Walking in the background. No lines. No arc. Present. Functional. Invisible."),
    ("👋 Level 2: Named But Barely", "You exist in the narrative. Someone said your name once. You had a reaction shot."),
    ("🗣️ Level 3: Recurring Background", "You show up consistently. People would notice if you were gone. You still don't have a subplot."),
    ("✨ Level 4: Fan Favorite Side Character", "You weren't supposed to be important. You became important. The fans want more."),
    ("🌟 Level 5: Surprise Main Character", "This was your story the whole time. You're just now realizing it. The camera is on you."),
]
if st.button("🎬 Assess My Background Energy", key="background_btn"):
    level, desc = random.choice(BACKGROUND_LEVELS)
    st.markdown(f"### {level}")
    st.info(desc)
st.markdown("---")

# ===== 146 =====
st.markdown("**— 146 —**")
st.subheader("Unhelpful Life Stages Timeline")
st.caption("when things are supposed to happen (they don't)")
LIFE_STAGES = [
    "Age 0-10: Blissful ignorance. Everything is new. Time moves like honey.",
    "Age 11-17: Convinced you understand everything. You understand nothing. This is important.",
    "Age 18-24: Freedom arrives. Accompanied immediately by consequences. Exciting. Terrifying.",
    "Age 25: The 'quarter life crisis' age. You've heard about this. You are currently in it.",
    "Age 30: Supposed to feel different. Doesn't feel different. Might feel different later.",
    "Age 35: Things make more sense OR you've accepted that they won't. Both are valid.",
    "Age 40: Allegedly the beginning. People in their 40s seem fine. Maybe even good.",
    "Age 50+: According to everyone who has been here: this is when it gets interesting.",
    "Age ???: You're somewhere on this line. Doing the thing. It counts.",
]
if st.button("📅 Find My Life Stage", key="lifestage_btn"):
    st.info(random.choice(LIFE_STAGES))
st.markdown("---")

# ===== 147 =====
st.markdown("**— 147 —**")
st.subheader("The 'Name Your Wi-Fi Something Threatening' Generator")
st.caption("for the neighbors")
WIFI_NAMES = [
    "FBI Surveillance Van #3",
    "Not Your Wi-Fi",
    "Tell My Wife I Love Her",
    "Loading...",
    "Searching...",
    "Pretty Fly for a Wi-Fi",
    "Bill Wi the Science Fi",
    "The LAN Before Time",
    "It Hurts When IP",
    "Wu-Tang LAN",
    "Router? I Hardly Know Her",
    "Silence of the LANs",
    "This Is Not a Wi-Fi",
    "Get Your Own Wi-Fi",
    "Winternet is Coming",
    "The Promise LAN",
    "No More Mr. Wi-Fi",
]
if st.button("📶 Name My Wi-Fi", key="wifi_btn"):
    name = random.choice(WIFI_NAMES)
    st.success(f"📶 **Network name:** {name}")
    st.code(name, language=None)
st.markdown("---")

# ===== 148 =====
st.markdown("**— 148 —**")
st.subheader("The 'Are You Procrastinating Right Now' Diagnostic")
st.caption("a brief self-assessment")
st.caption("(the fact that you're on this website is already data)")
if st.button("🔬 Run Diagnostic", key="proc_diag_btn"):
    with st.spinner("analyzing behavior patterns..."):
        time.sleep(1.5)
    results = [
        ("YES — High Confidence", "You are on a website called Dumb Stuff instead of doing the thing. The diagnostic is complete."),
        ("YES — Definitively", "The thing exists. You are not doing it. You are here instead. This is procrastination."),
        ("PROBABLY YES", "Even if you don't have a thing, you could be resting more intentionally. This is still avoidance-adjacent."),
        ("INCONCLUSIVE — But Likely Yes", "You pressed a button to find out if you're procrastinating instead of just... not procrastinating. Think about that."),
    ]
    label, desc = random.choice(results)
    st.markdown(f"### Diagnosis: {label}")
    st.warning(desc)
st.markdown("---")

# ===== 149 =====
st.markdown("**— 149 —**")
st.subheader("The Comfort Tier List")
st.caption("things that bring comfort, ranked")
COMFORT_ITEMS = [
    ("S tier ✨", "Your specific blanket. Not just any blanket. THE blanket."),
    ("S tier ✨", "Hot drink in a good mug. The mug matters. You have one."),
    ("A tier", "Rain on a window when you're inside. Nature doing something dramatic on your behalf."),
    ("A tier", "The first five minutes of a comfort rewatch. Before anything bad happens yet."),
    ("B tier", "A familiar smell in an unexpected place. Temporal displacement, brief and pleasant."),
    ("B tier", "Finding money in a pocket you forgot about. Unexpected surplus."),
    ("C tier", "New socks. Clean. Not worn yet. The potential of them."),
    ("C tier", "The silence after a difficult thing is done."),
    ("D tier", "The snooze button. Comforting in the moment. Complicated shortly after."),
]
for tier, item in COMFORT_ITEMS:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"**{tier}**")
    with col2:
        st.caption(item)
st.markdown("---")

# ===== 150 =====
st.markdown("**— 150 —**")
st.subheader("🎊 Milestone: Feature 150")
st.caption("halfway to 300. or an end point. either works.")
if st.button("🎊 Celebrate Feature 150", key="f150_btn"):
    st.balloons()
    st.success("""
🎊 150 FEATURES 🎊

You have now scrolled through 150 features on a website called Dumb Stuff.

At some point this stopped being about the features.
This is about you now.
What are you looking for?
Whatever it is, we hope you find it.
Or find it good enough.
Or decide you didn't need it.

All three outcomes are valid.

Go drink some water.
You've earned it.
    """)

# ============ FEATURES 151–200 ============

# ===== 151 =====
st.markdown("**— 151 —**")
st.subheader("The 'Describe Your Personality as a Font'")
st.caption("typography as identity")
FONT_PERSONALITIES = [
    ("Times New Roman", "Classic. Reliable. Slightly formal even in casual settings. Been around forever. Still respected."),
    ("Comic Sans", "Chaotic good. Refuses to take things too seriously. Deeply misunderstood. Has haters. Doesn't care."),
    ("Helvetica", "Clean. Confident. No unnecessary flourishes. Everything in its right place. Slightly intimidating."),
    ("Papyrus", "Trying to communicate depth and mystery. The depth is there. The execution is contested."),
    ("Wingdings", "Entirely encoded. Not immediately readable. Reveals itself slowly. Worth deciphering."),
    ("Impact", "LOUD IN A VERY SPECIFIC CONTEXT. Quieter in person. The all-caps is a persona."),
    ("Garamond", "Elegant. Old soul. Thoughtful spacing. The kind of person who takes their time and it shows."),
    ("Courier New", "Straight-talking. Monospaced. Every character gets equal room. Fair. Slightly retro."),
]
if st.button("🔤 Find My Font", key="font_btn"):
    font, desc = random.choice(FONT_PERSONALITIES)
    st.markdown(f"### You are: {font}")
    st.info(desc)
st.markdown("---")

# ===== 152 =====
st.markdown("**— 152 —**")
st.subheader("The 'Things That Slap Differently at Night'")
st.caption("the nocturnal upgrade")
NIGHT_THINGS = [
    "Cereal at 2am hits differently than cereal at 8am. This is not nutrition. This is an experience.",
    "The same playlist you listen to during the day becomes a completely different emotional journey after 11pm.",
    "Texting someone at 1am carries a weight that the same text at 2pm simply does not have.",
    "The city sounds at 3am — fewer of them, further apart — create a silence that the day never allows.",
    "A walk at night when the streets are empty is a completely different activity than a walk at noon.",
    "Problems seem bigger at night. They are not bigger. They are the same size. The context is different.",
    "Leftover food at midnight is a completely different meal than the same food at 7pm.",
    "The version of yourself that exists between 11pm and 2am has thoughts and opinions the daytime version won't remember.",
]
if st.button("🌙 What Slaps at Night?", key="night_btn"):
    st.info(f"🕯️ {random.choice(NIGHT_THINGS)}")
st.markdown("---")

# ===== 153 =====
st.markdown("**— 153 —**")
st.subheader("The 'Rename Your Group Chat' Generator")
st.caption("your group chat deserves a better name")
GROUP_CHAT_NAMES = [
    "The Council of Nothing in Particular",
    "Active Between 11pm and 3am Only",
    "We Said We'd Meet Up",
    "Nobody Reads This Anymore",
    "Core Four (There Are Seven of Us)",
    "The Original Group (We Splintered)",
    "Support Group for Being Normal",
    "We Met At That Thing",
    "Everyone Is Fine Here",
    "Meme Repository and Occasional Feelings",
    "The Ones Who Actually Showed Up",
    "Inside Jokes: The Group Chat",
    "This Was Active in 2019",
    "Family (We Don't Choose)",
    "The Chaos Channel",
    "People I Would Call If Needed",
]
if st.button("💬 Rename My Group Chat", key="groupchat_btn"):
    name = random.choice(GROUP_CHAT_NAMES)
    st.success(f"📱 **New group name:** {name}")
    st.code(name, language=None)
st.markdown("---")

# ===== 154 =====
st.markdown("**— 154 —**")
st.subheader("The Passive Voice Apology Generator")
st.caption("mistakes were made")
PASSIVE_APOLOGIES = [
    "Mistakes were made, and they were made near me, by forces largely outside of anyone's direct control.",
    "It has come to my attention that feelings may have been hurt. This was not the intention of the involved parties.",
    "Errors were made in the communication of certain information. Steps are being taken to ensure nothing changes.",
    "The situation that occurred was unfortunate. Lessons have been identified. They will be forgotten by next week.",
    "Words were said. They were heard differently than they were meant. The gap between intent and impact has been noted.",
    "The incident is regretted. The incident will not be repeated, provided similar circumstances do not arise.",
    "Inconvenience was caused. Inconvenience was experienced. Both of these facts are acknowledged without further elaboration.",
]
if st.button("🤷 Generate Passive Apology", key="passive_apology_btn"):
    st.info(f"📋 {random.choice(PASSIVE_APOLOGIES)}")
st.markdown("---")

# ===== 155 =====
st.markdown("**— 155 —**")
st.subheader("The Fridge Leftovers Personality Test")
st.caption("what does your fridge say about you")
FRIDGE_PROFILES = [
    "Your fridge has: 3 condiments, half an onion, and something in the back you're not ready to investigate. You are a person who intends to cook more than you do.",
    "Your fridge has: meal-prepped containers for every day this week. You are either thriving or you're performing thriving. Both are valid.",
    "Your fridge has: exclusively beverages and one sad piece of fruit. You eat out a lot. You feel fine about this.",
    "Your fridge has: leftovers from 3 different restaurants all in different states of viability. You're an optimist.",
    "Your fridge has: everything you need to cook a specific recipe you saw online 6 days ago and haven't made yet.",
    "Your fridge is nearly empty. Not because of chaos — because you've mastered buying only what you'll actually eat. Rare. Respected.",
    "Your fridge has: something mysterious on the second shelf. You know what it is. You are not ready.",
]
if st.button("🧊 Read My Fridge", key="fridge_btn"):
    st.info(f"❄️ {random.choice(FRIDGE_PROFILES)}")
st.markdown("---")

# ===== 156 =====
st.markdown("**— 156 —**")
st.subheader("Unsolicited Movie Review for Your Day")
st.caption("★★★☆☆")
DAY_REVIEWS = [
    "★★★☆☆ Today was a solid middle entry in the ongoing series. Not the best episode. Certainly not the worst. Watchable. Would experience again.",
    "★★☆☆☆ Slow start. Unclear middle. Abrupt ending. The snack was good. Two stars.",
    "★★★★☆ Surprising depth for what looked like a routine day. The third act had an unexpected moment. Recommend.",
    "★☆☆☆☆ Did not meet expectations. Expectations were low. Still missed them. One star. Moving on.",
    "★★★★★ Underrated. Nobody will talk about this day but it was genuinely good. The coffee was right. The light was nice. Moments happened.",
    "★★★☆☆ Technically competent. Narratively familiar. Competent execution of a standard premise. Better than nothing.",
    "★★☆☆☆ The first half promised more than the second half delivered. The ending was just stopping.",
]
if st.button("🎬 Review My Day", key="dayreview_btn"):
    st.warning(f"🍿 {random.choice(DAY_REVIEWS)}")
st.markdown("---")

# ===== 157 =====
st.markdown("**— 157 —**")
st.subheader("The 'Name That Anxiety' Clinic")
st.caption("identifying the specific flavor of your worry")
ANXIETY_TYPES = [
    ("The Anticipation Spiral", "Something is coming. It might be fine. You are treating it as if it will not be fine. Preemptive suffering."),
    ("The Retroactive Cringe", "Something happened days ago. You are relitigating it. The other person has moved on. You have not been informed."),
    ("The Low-Grade Background Hum", "Nothing specific. Just: a general awareness that things exist and could go wrong. Ambient worry."),
    ("The Productivity Guilt", "You're resting. You feel guilty about resting. The guilt prevents proper rest. The cycle is self-sustaining."),
    ("The Social Replay Loop", "Something you said in a conversation. On a loop. Slightly edited each time. Getting worse."),
    ("The Future Debt Anxiety", "Not a current problem. A future problem. You're borrowing worry from next month."),
    ("The 'Did I Hurt Them' Check", "Something you said or didn't say. They seemed fine. You are not sure they were fine."),
    ("The Decision Paralysis", "Two options. Both fine. You cannot move until you know which is better. Neither is better."),
]
if st.button("🩺 Diagnose My Anxiety Type", key="anxtype_btn"):
    kind, desc = random.choice(ANXIETY_TYPES)
    st.markdown(f"### {kind}")
    st.info(desc)
    st.caption("(name it to tame it. or just name it. naming is enough for now.)")
st.markdown("---")

# ===== 158 =====
st.markdown("**— 158 —**")
st.subheader("Imaginary Book Titles")
st.caption("books that should exist")
BOOK_TITLES = [
    "📚 *The Fine Art of Doing Nothing Intentionally* — a practical guide",
    "📚 *Per My Last Email: A Memoir of Corporate Survival* — nonfiction",
    "📚 *The Middle Shelf: A Life Between Done and Not Started* — literary fiction",
    "📚 *Everything Is Fine (And Other Things I Tell Myself)* — essays",
    "📚 *You're Not Behind: A Timeline of People Who Figured It Out Late* — inspirational nonfiction",
    "📚 *The Snooze Button Chronicles* — a love story",
    "📚 *Functional Chaos: How to Thrive in Mild Disorder* — self-help",
    "📚 *The Group Chat: Stories from the Modern Village* — short fiction",
    "📚 *Adequate: A Guide to Being Good Enough at Most Things* — practical wisdom",
    "📚 *The 2am Version of Yourself* — poetry collection",
]
if st.button("📖 Read a Fake Book Title", key="booktitle_btn"):
    st.success(random.choice(BOOK_TITLES))
st.markdown("---")

# ===== 159 =====
st.markdown("**— 159 —**")
st.subheader("The 'Describe Your Energy Today in One Meal'")
st.caption("food as emotional data")
ENERGY_MEALS = [
    ("🥣 Plain oatmeal", "Functional. Getting through it. Nutritionally sufficient. Nobody's favorite but it does the job."),
    ("🍕 Cold leftover pizza at 11am", "You're doing things your own way. Unconventional. Surprisingly satisfying."),
    ("🥗 Salad you actually wanted", "Something has shifted. You wanted the salad. This is growth."),
    ("🍜 Instant noodles at midnight", "Comfort mode. Low effort, high warmth. No judgment from the noodles."),
    ("🧇 Full breakfast on a Tuesday", "You've decided today matters. You made eggs. You are the main character."),
    ("🍫 Chocolate for breakfast", "You've made peace with something. The day begins now, on your terms."),
    ("🥐 Croissant from a good bakery", "Treating yourself. Small luxury. Well deserved. You walked to get it."),
    ("🍵 Just tea, nothing else", "Contemplative. Minimalist. Either resting or preparing. Both are valid."),
]
if st.button("🍽️ What Meal Am I Today?", key="mealenergy_btn"):
    meal, desc = random.choice(ENERGY_MEALS)
    st.markdown(f"### {meal}")
    st.info(desc)
st.markdown("---")

# ===== 160 =====
st.markdown("**— 160 —**")
st.subheader("Extremely Long Loading Bar (Goes Nowhere)")
st.caption("the journey is the destination")
if st.button("⏳ Start the Long Load", key="longload_btn"):
    bar = st.progress(0)
    status = st.empty()
    steps = [
        (10, "Initializing your vibe..."),
        (23, "Loading personality modules..."),
        (31, "Calibrating expectations..."),
        (44, "Consulting the void..."),
        (52, "Downloading motivation (slow connection)..."),
        (61, "Compiling your unfinished projects..."),
        (74, "Rendering your 2am thoughts..."),
        (83, "Almost there..."),
        (91, "Still almost there..."),
        (97, "So close..."),
        (99, "One more second..."),
    ]
    for pct, msg in steps:
        status.text(msg)
        bar.progress(pct)
        time.sleep(0.4)
    time.sleep(0.8)
    bar.progress(100)
    status.success("Done. Nothing loaded. You waited anyway. Respect.")
st.markdown("---")

# ===== 161 =====
st.markdown("**— 161 —**")
st.subheader("The Philosophical Hot Dog Debate")
st.caption("the question that started it all")
if st.button("🌭 Is a Hot Dog a Sandwich?", key="hotdog_btn"):
    positions = [
        ("YES — It's a Sandwich", "Bun = bread. Filling = inside. This is a sandwich. The hinge is irrelevant. The definition holds."),
        ("NO — It's a Hot Dog", "A hot dog is a hot dog. It exists as its own category. Calling it a sandwich is technically correct and socially unacceptable."),
        ("IT'S COMPLICATED", "The hot dog exists in a liminal space between sandwich and taco (folded = taco). It is its own thing. Language is insufficient."),
        ("THE QUESTION IS WRONG", "The real question is: who decided sandwiches needed a definition? Let the hot dog be free."),
    ]
    label, argument = random.choice(positions)
    st.markdown(f"### Position: {label}")
    st.info(argument)
    st.caption("this debate has no correct answer. that is the point.")
st.markdown("---")

# ===== 162 =====
st.markdown("**— 162 —**")
st.subheader("Name That Sound")
st.caption("onomatopoeia for things that don't have words")
SOUND_NAMES = [
    ("The soft thud of a book falling off a table at night", "Suggested name: *Flopf*. Hollow. Soft. Final."),
    ("The creak of a floor when you're trying to be quiet", "Suggested name: *Skreeee*. Betrayal noise. You were so careful."),
    ("The sound of a bag of chips opening", "Suggested name: *Crshhh*. Loud. Inevitable. The room now knows."),
    ("The specific beep of a microwave at 1am", "Suggested name: *Beepf*. Three notes. Carries through walls."),
    ("The sound right before your phone dies", "Suggested name: *Doomtick*. One final buzz. Then silence."),
    ("The squeak of a marker on a whiteboard", "Suggested name: *Screek*. Causes involuntary reactions in 90% of people."),
    ("The sound of ice in a drink settling", "Suggested name: *Clinktink*. Small. Satisfying. Announces readiness."),
    ("The whoosh of an email being sent", "Suggested name: *Whooomp*. Committed. Cannot be undone. The sound of no return."),
]
if st.button("🔊 Name a Sound", key="sound_name_btn"):
    sound, name = random.choice(SOUND_NAMES)
    st.markdown(f"**Sound:** {sound}")
    st.info(f"**Name:** {name}")
st.markdown("---")

# ===== 163 =====
st.markdown("**— 163 —**")
st.subheader("The 'Describe Your Vibe as a Room'")
st.caption("interior design as personality")
ROOM_VIBES = [
    "You're a warm kitchen at 9pm — something's been cooking, it smells good, the light is right, nobody wants to leave.",
    "You're a home library nobody uses but everyone loves — full of potential, slightly dusty, very meaningful.",
    "You're a living room mid-renovation — work in progress, clearly going somewhere good, slightly chaotic right now.",
    "You're a corner café table — consistent presence, reliable, slightly removed from the action, observing everything.",
    "You're a sunlit bedroom on a day off — no schedule, soft light, no reason to be anywhere else.",
    "You're a well-stocked basement workshop — tools for everything, organized in a way only you understand, deeply useful.",
    "You're a hotel lobby at 6am — awake before the rest, quiet, functioning, waiting for the day to begin.",
    "You're a rooftop at golden hour — elevated, warm, the best version of the day, slightly hard to reach but worth it.",
]
if st.button("🏠 What Room Am I?", key="room_btn"):
    st.info(f"🛋️ {random.choice(ROOM_VIBES)}")
st.markdown("---")

# ===== 164 =====
st.markdown("**— 164 —**")
st.subheader("The Extremely Niche True Crime Podcast")
st.caption("crimes too small for major networks")
NICHE_CRIMES = [
    "🎙️ *The Last Cookie*: Someone took the final cookie without noting it on the shared snack board. The investigation begins.",
    "🎙️ *Reply All*: A forensic look at the 2019 company-wide email chain that spiraled out of control. 47 episodes.",
    "🎙️ *The Parking Spot Incident*: This was clearly someone else's spot. The CCTV footage is inconclusive.",
    "🎙️ *Cold Case: The Missing Tupperware*: It's been in someone's cabinet for 3 years. They know who they are.",
    "🎙️ *The Wifi Password*: Changed without notice. No announcement. Devices disconnected. Someone is responsible.",
    "🎙️ *Empty*: Who put the empty carton back in the fridge? A 12-part series. No resolution.",
    "🎙️ *The Noise Complaint*: A documentary about a single neighbor and the sounds they make at 11pm. Emotional.",
    "🎙️ *The Thermostat Wars*: An ongoing conflict spanning years. Multiple parties. No consensus.",
]
if st.button("🎙️ Play a Niche True Crime Podcast", key="truecrime_btn"):
    st.info(random.choice(NICHE_CRIMES))
st.markdown("---")

# ===== 165 =====
st.markdown("**— 165 —**")
st.subheader("The 'Describe Your Ideal Day' but Honest")
st.caption("what you'd actually do with a free day")
IDEAL_DAYS = [
    "Wake up with no alarm. Lie there for a while. Have breakfast slowly. No agenda. No notifications. Something cozy. Nap. End.",
    "Do exactly one (1) productive thing and then call it. Feel excellent about this. The one thing was enough. It is always enough.",
    "Read something good. Eat something good. Talk to someone who makes it easy. Be home before it gets late.",
    "Move around a bit. Outside for a while. Then inside. Food at the right time. Evening with something good on. Sleep.",
    "Nothing specific. No plans. Decide in real time what sounds good. Follow that. Repeat until evening.",
    "A walk. Some music. Good coffee. Long unstructured time. A comfortable place to sit. Low stakes. High satisfaction.",
    "Stay in. Have an excellent day without leaving. Clean something if the mood strikes. Watch something. Eat well. Exist.",
    "Be somewhere nice. Not do much there. That's it.",
]
if st.button("🌅 Describe My Ideal Day", key="idealday_btn"):
    st.info(f"🌿 {random.choice(IDEAL_DAYS)}")
st.markdown("---")

# ===== 166 =====
st.markdown("**— 166 —**")
st.subheader("The Cheese Alignment Chart")
st.caption("cheese as philosophy")
CHEESE_ALIGNMENT = [
    ("🧀 Cheddar", "Lawful Good. Reliable. Does what it says. Sharp or mild. Both acceptable. No surprises."),
    ("🧀 Brie", "Chaotic Good. Soft exterior, complex interior. Gets better at room temperature. Elegant chaos."),
    ("🧀 Parmesan", "Lawful Neutral. Hard. Aged. Does everything better in small amounts. Respected universally."),
    ("🧀 Gouda", "Neutral Good. Warm. Agreeable. Smoked version has a whole other energy. Easy to love."),
    ("🧀 Blue Cheese", "Chaotic Neutral. Polarizing. Intense. Wrong to some. Essential to others. No middle ground."),
    ("🧀 Swiss", "True Neutral. The mediator of cheeses. Present on everything. Offends no one. Noticed by few."),
    ("🧀 Pepper Jack", "Chaotic Neutral leaning Chaotic Good. Has opinions. Makes its presence known. Great on sandwiches."),
    ("🧀 Velveeta", "Lawful Evil. Technically cheese-adjacent. Used in things you love. You don't ask questions."),
]
if st.button("🧀 Find My Cheese Alignment", key="cheese_btn"):
    cheese, alignment = random.choice(CHEESE_ALIGNMENT)
    st.markdown(f"### {cheese}")
    st.info(alignment)
st.markdown("---")

# ===== 167 =====
st.markdown("**— 167 —**")
st.subheader("What Your Texting Habits Say About You")
st.caption("digital body language analysis")
TEXTING_HABITS = [
    ("You send multiple short texts in a row", "Stream of consciousness. Real-time thinker. The conversation happens in multiple installments."),
    ("You write long detailed texts", "You draft things. You consider. You want to be understood correctly the first time."),
    ("You use voice messages", "Efficiency-focused OR you have a lot to say and typing feels slow. Either way: controversial."),
    ("You reply instantly, always", "Always near your phone. High availability. Might need a notification-free hour."),
    ("You reply after a few hours consistently", "You process first, respond second. Batched communication. Very sane."),
    ("You sometimes take days to reply", "Overwhelmed OR selective. Replies always meaningful when they arrive."),
    ("You use no punctuation in texts", "Casual. Fast. The absence of periods is not rudeness. It's just texting."),
    ("You use full punctuation always", "Either very formal or you write texts the way you'd write everything. Both understandable."),
]
if st.button("💬 Analyze My Texting Style", key="textstyle_btn"):
    style, analysis = random.choice(TEXTING_HABITS)
    st.markdown(f"**Style:** {style}")
    st.info(analysis)
st.markdown("---")

# ===== 168 =====
st.markdown("**— 168 —**")
st.subheader("The Bad Advice Machine")
st.caption("technically advice. not recommended.")
BAD_ADVICE = [
    "If you're running late, go faster. This solves the lateness.",
    "If you can't sleep, just close your eyes and lie there and eventually it will happen. (It takes forever. This is correct.)",
    "If you're hungry, eat something. We can't stress this enough.",
    "If you're cold, put on a layer. Groundbreaking.",
    "The best time to start was earlier. The second best time is now. The third best time is tomorrow. The fourth is next week. Pick one.",
    "Have you considered simply not worrying about it? No? Okay. The advice stands.",
    "If you're tired and you can sleep, sleep. If you can't sleep, that's a different problem that we also don't know how to solve.",
    "Just be yourself, but better. More put-together. Also more relaxed. These are compatible.",
    "Think less. Also think more. About the right things. Stop thinking about the wrong things. You know which is which.",
]
if st.button("💡 Get Bad Advice", key="badadvice_btn"):
    st.warning(f"📋 {random.choice(BAD_ADVICE)}")
st.markdown("---")

# ===== 169 =====
st.markdown("**— 169 —**")
st.subheader("Words That Should Exist But Don't")
st.caption("proposing additions to the dictionary")
PROPOSED_WORDS = [
    ("Glurch (n.)", "The specific feeling of getting something sticky on your hands unexpectedly."),
    ("Frempt (v.)", "To start cleaning something and make it temporarily much worse before it gets better."),
    ("Snorvel (n.)", "The specific noise your stomach makes at the worst possible moment."),
    ("Quibbet (n.)", "The small piece of a sticker that remains on a surface no matter how carefully you peel."),
    ("Frumple (v.)", "To re-read something multiple times because your brain keeps refusing to process it."),
    ("Snorgle (v.)", "To press your face into something soft and comforting (a pet, a pillow) for relief."),
    ("Blurk (n.)", "The sound of something that should be silent making an unexpected noise."),
    ("Glumf (n.)", "The feeling of waking up in the middle of a good dream."),
    ("Wumple (v.)", "To try to fold a fitted sheet and give up after two attempts."),
    ("Snerp (n.)", "The specific sound of opening a can of something fizzy."),
]
if st.button("📖 Add a Word to the Dictionary", key="newword_btn"):
    word, definition = random.choice(PROPOSED_WORDS)
    st.markdown(f"### {word}")
    st.info(definition)
st.markdown("---")

# ===== 170 =====
st.markdown("**— 170 —**")
st.subheader("The 'Translate This Passive Aggression' Button")
st.caption("decoding the subtext")
PA_TRANSLATIONS = [
    ("'I guess that works.'", "It does not work. They have accepted that you will not change it. They are noting their dissatisfaction for the record."),
    ("'No, it's fine.'", "Chronological: it was not fine, it is not fine, it will not be fine. The word 'fine' is load-bearing and collapsing."),
    ("'I already handled it.'", "They handled something you were supposed to handle. They will not forget this. It will appear in a future conversation."),
    ("'Good to know.'", "This is not good. They have learned something they did not want to learn. They are cataloguing it."),
    ("'Interesting choice.'", "They disagree with the choice. They will not tell you why. You will find out later through consequences."),
    ("'I'll let you figure it out.'", "They know the answer. They've decided not to share it. The reason is complicated."),
    ("'Whatever you think is best.'", "They have an opinion. They've decided you don't deserve it. Proceed carefully."),
]
if st.button("🔍 Decode Passive Aggression", key="decode_pa_btn"):
    phrase, translation = random.choice(PA_TRANSLATIONS)
    st.markdown(f"**They said:** *\"{phrase}\"*")
    st.error(f"**They meant:** {translation}")
st.markdown("---")

# ===== 171 =====
st.markdown("**— 171 —**")
st.subheader("The 'Assign a Movie Genre to Your Current Mood'")
st.caption("what kind of film are you living right now")
MOOD_GENRES = [
    ("🎬 Slow Cinema", "Not much is happening but it feels significant. Long takes. Meaningful silence."),
    ("🎬 Heist Movie", "You're planning something. Multiple steps. People are involved. It will either work perfectly or go completely sideways."),
    ("🎬 Documentary", "Observational mode. Watching things happen. Occasionally narrating internally. Forming conclusions."),
    ("🎬 Romantic Comedy Third Act", "Something almost went wrong. Or did go wrong. But it's probably going to be fine. You're almost there."),
    ("🎬 Horror (Psychological)", "Everything looks normal. Something is slightly off. You can't identify what. You're not sure you want to."),
    ("🎬 Sports Movie Underdog Arc", "You've been counted out. The training montage is happening. People will be surprised."),
    ("🎬 Slice of Life Indie", "Nothing dramatic. Small moments. Ordinary life filmed with care. Actually kind of beautiful."),
    ("🎬 Sequel Nobody Asked For", "This has happened before. Similar plot. Minor differences. You're going through it again with more experience."),
]
if st.button("🎞️ What Genre Is My Mood?", key="moodgenre_btn"):
    genre, desc = random.choice(MOOD_GENRES)
    st.markdown(f"### {genre}")
    st.info(desc)
st.markdown("---")

# ===== 172 =====
st.markdown("**— 172 —**")
st.subheader("The Commitment Level Analyzer")
st.caption("how committed are you, really")
COMMITMENTS = [
    ("📅 You saved an event to your calendar", "Interested. Not confirmed. 40% chance of attending."),
    ("📅 You said 'sounds fun!'", "Positive reception. No commitment implied. 25% chance."),
    ("📅 You said 'I'll be there'", "Intention stated. Life may intervene. 70% chance."),
    ("📅 You asked 'what should I bring?'", "High commitment. You are going. 90% chance."),
    ("📅 You made plans to make plans", "Preliminary interest. This will require follow-up. Outcome unknown."),
    ("📅 You already left the house", "100% committed. You are there. You cannot undo this."),
    ("📅 You said 'maybe'", "This is a polite no. Both parties know this. The fiction is maintained for everyone's comfort."),
]
if st.button("📊 Analyze My Commitment", key="commit_btn"):
    level, analysis = random.choice(COMMITMENTS)
    st.markdown(f"**Level:** {level}")
    st.info(analysis)
st.markdown("---")

# ===== 173 =====
st.markdown("**— 173 —**")
st.subheader("Random Compliment in Another Language")
st.caption("you are appreciated, internationally")
INTL_COMPLIMENTS = [
    ("Spanish 🇪🇸", "Eres increíble", "You are incredible"),
    ("French 🇫🇷", "Tu es formidable", "You are wonderful"),
    ("Italian 🇮🇹", "Sei fantastico/a", "You are fantastic"),
    ("Portuguese 🇧🇷", "Você é incrível", "You are incredible"),
    ("German 🇩🇪", "Du bist wunderbar", "You are wonderful"),
    ("Japanese 🇯🇵", "素晴らしいです", "You are splendid"),
    ("Korean 🇰🇷", "대단해요", "You are amazing"),
    ("Mandarin 🇨🇳", "你真的很棒", "You are truly great"),
    ("Dutch 🇳🇱", "Je bent geweldig", "You are amazing"),
    ("Swedish 🇸🇪", "Du är fantastisk", "You are fantastic"),
]
if st.button("🌍 International Compliment", key="intl_btn"):
    flag_lang, phrase, meaning = random.choice(INTL_COMPLIMENTS)
    st.success(f"**{flag_lang}:** {phrase}")
    st.caption(f"*(Translation: {meaning})*")
st.markdown("---")

# ===== 174 =====
st.markdown("**— 174 —**")
st.subheader("The Overly Long Receipt for a Simple Purchase")
st.caption("you bought one thing")
if st.button("🧾 Generate the Receipt", key="longrec_btn"):
    now = datetime.datetime.now()
    st.code(f"""
TRANSACTION RECEIPT
{now.strftime('%Y-%m-%d %H:%M:%S')}
Store: Somewhere You Went

Item: {random.choice(['Coffee', 'Snack', 'One (1) thing', 'Something small'])}
Qty: 1
Price: ${random.randint(3,8)}.{random.randint(10,99)}

Subtotal: calculated
Tax (complex): applied
Possible surcharge: maybe
Adjustment: yes
Pre-discount total: higher
Discount: minimal
Final total: what you paid

Points earned: 47
Points needed for reward: 4,800
Estimated time to reward: never

SURVEY CODE: NOPE-1234-ABCD
Complete survey for 5% off next visit
(offer expires in 48 hours)
(survey takes 12 minutes)

Thank you for your purchase.
Have a great day.
Have a great rest of your day.
Have a great rest of your week.
We appreciate your business.
Come back soon.
Seriously, come back.

--- END OF RECEIPT ---
""", language=None)
st.markdown("---")

# ===== 175 =====
st.markdown("**— 175 —**")
st.subheader("Cursed Riddles")
st.caption("the answer makes sense and also doesn't")
RIDDLES = [
    ("I have cities, but no houses live there. I have mountains, but no trees grow there. I have water, but no fish swim there. What am I?",
     "A map. Although honestly this riddle is about maps lying to us."),
    ("The more you take, the more you leave behind. What am I?",
     "Footsteps. Or decisions. Or emails. Multiple correct answers."),
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
     "An echo. Or your Zoom avatar unmuting unexpectedly."),
    ("What has hands but can't clap?",
     "A clock. Also, technically, some people at certain concerts."),
    ("I'm always in front of you but can't be seen. What am I?",
     "The future. Or your blind spot. Or whatever you're avoiding looking at."),
    ("The more you dry me, the wetter I become. What am I?",
     "A towel. Also, ironically, certain work environments."),
]
if st.button("🧩 Give Me a Riddle", key="riddle_btn"):
    q, a = random.choice(RIDDLES)
    st.markdown(f"**Riddle:** {q}")
    with st.spinner("thinking..."):
        time.sleep(1.5)
    st.success(f"**Answer:** {a}")
st.markdown("---")

# ===== 176 =====
st.markdown("**— 176 —**")
st.subheader("The LinkedIn Headline Generator (Absurd Edition)")
st.caption("personal branding for the unbranded")
LINKEDIN_HEADLINES = [
    "Passionate Human | Living Life | Open to Opportunities That Don't Exist Yet",
    "Strategic Napper | Snack Curator | Aspiring Person Who Has It Together",
    "Results-Driven Individual | Currently Between Epiphanies | 500+ Thoughts",
    "Visionary | Dreamer | Someone Who Googled 'What Is a Thought Leader' Last Week",
    "Chief Breakfast Officer | B2B (Bed to Breakfast) | Scaling Comfort Operations",
    "Disrupting the Status Quo of Just Sitting Here | Innovation Adjacent | Available",
    "10x Person (Self-Assessed) | Synergy Survivor | Building Something Unclear",
    "Ex-Person Who Had It Together | Current: Figuring It Out | Hiring Myself",
    "Leveraging My Authentic Self to Deliver Value to My Own Life | Open to Connections",
    "Passionate About [REDACTED] | Expert in Figuring It Out | Growth Mindset (Allegedly)",
]
if st.button("💼 Generate My LinkedIn Headline", key="linkedin_btn"):
    headline = random.choice(LINKEDIN_HEADLINES)
    st.success(f"**Your headline:** {headline}")
    st.code(headline, language=None)
st.markdown("---")

# ===== 177 =====
st.markdown("**— 177 —**")
st.subheader("The 'No Thoughts, Head Empty' Content Generator")
st.caption("nothing here. just vibes.")
EMPTY_CONTENT = [
    "🧠 [no thoughts. just the ambient sound of existing.]",
    "🧠 [brain screensaver mode. the fish are swimming. no one is home.]",
    "🧠 [buffering... please enjoy this moment of white noise while we locate your thoughts]",
    "🧠 [content not found. have you tried having fewer tabs open?]",
    "🧠 [this thought space intentionally left blank]",
    "🧠 [404: thoughts not found. redirecting to snack consideration.]",
    "🧠 [the monkey that runs the brain is on break. back in 20.]",
    "🧠 [no input received. no output available. just vibes.]",
]
if st.button("🧠 Access the Empty Head", key="empty_btn"):
    st.info(random.choice(EMPTY_CONTENT))
st.markdown("---")

# ===== 178 =====
st.markdown("**— 178 —**")
st.subheader("The 'Name a Dog' Generator")
st.caption("for an imaginary dog you may one day have")
DOG_NAMES_A = ["Sir", "Lady", "Professor", "Captain", "Doctor", "Duchess", "Baron", "Admiral"]
DOG_NAMES_B = ["Biscuit", "Meatball", "Waffle", "Noodle", "Pretzel", "Dumpling", "Crouton", "Pudding", "Cobbler", "Brisket"]
DOG_NAMES_C = ["the Third", "Esq.", "PhD", "of the Valley", "the Magnificent", "von Floof", "the Brave", "of Chaos"]
if st.button("🐕 Name My Future Dog", key="dogname_btn"):
    name = f"{random.choice(DOG_NAMES_A)} {random.choice(DOG_NAMES_B)} {random.choice(DOG_NAMES_C)}"
    st.success(f"🐾 **Your dog's name:** {name}")
    st.caption("this dog deserves the name. they will grow into it.")
st.markdown("---")

# ===== 179 =====
st.markdown("**— 179 —**")
st.subheader("The 'Describe Your Last Dream' But Make It a Movie Pitch")
st.caption("your subconscious is a writer")
DREAM_PITCHES = [
    "A man must navigate a building that keeps adding new floors. He has a very important appointment on floor 47. The elevator only goes to 44.",
    "She's at her old high school, but she's an adult now, and there's an exam she forgot to study for, and everyone knows.",
    "He's late to something important but every time he gets near the destination, he's somewhere different. He never arrives. He wakes up.",
    "A woman is flying, but only barely above the ground, and only if she concentrates very hard. The moment she thinks about it too much, she lands.",
    "He's in his childhood home, but rooms keep appearing that weren't there before. The rooms aren't threatening. They're just... extra.",
    "She needs to make a phone call. She cannot remember the number. She cannot dial properly. The phone keeps changing.",
    "Everyone he knows is at a party in a house he's never been to. He's welcome. He knows no one. Everything is fine. It's somehow not fine.",
    "There's an animal in the house. It's fine. It belongs there. Nobody questions it. It's enormous. Nobody mentions it.",
]
if st.button("🎬 Pitch My Dream", key="dreampitch_btn"):
    st.success(f"💭 {random.choice(DREAM_PITCHES)}")
st.markdown("---")

# ===== 180 =====
st.markdown("**— 180 —**")
st.subheader("The Absurd Cooking Show Challenge")
st.caption("today's mystery basket contains...")
MYSTERY_BASKETS = [
    "Your mystery ingredients: one sad carrot, the last of the hot sauce, some pasta that might be expired, and whatever's left in the butter.",
    "Today's challenge: make something impressive using only what you actually have right now. Timer starts now.",
    "Mystery basket: half a lemon, questionable cheese, three eggs, and the emotional weight of a Tuesday.",
    "You have: everything for a great meal except one key ingredient. Adapt. The judges are watching.",
    "Today's basket contains: leftovers from two different meals that didn't finish, and optimism.",
    "Your ingredients: the thing you bought with good intentions, the thing that's been in the back of the cabinet for a year, and time.",
    "Mystery basket: a spice blend you don't fully understand, something frozen, and a vague sense that this could work.",
    "Today's challenge: cook something with what you have without going to the store. The store is very close. You will not go.",
]
if st.button("👨‍🍳 Open the Mystery Basket", key="cookshow_btn"):
    with st.spinner("judges are deliberating..."):
        time.sleep(0.8)
    st.warning(f"🥘 {random.choice(MYSTERY_BASKETS)}")
st.markdown("---")

# ===== 181 =====
st.markdown("**— 181 —**")
st.subheader("The 'Explain Your Password Hint' to a Stranger")
st.caption("completely made up, obviously")
PASSWORD_HINTS = [
    "Hint: 'the summer thing' — you know exactly what this means. A stranger would have no idea. Perfect security.",
    "Hint: 'mom's first car + number' — secure. Also you will forget which number. It happens every time.",
    "Hint: 'first pet + year' — your first pet was named something extremely guessable. The year does not help.",
    "Hint: 'favorite food + !' — there are 14 characters in 'pizza!' that someone could try. You feel safe. You are fine.",
    "Hint: 'the thing from 2015' — there were several things in 2015. This hint is for you only. Excellent.",
    "Hint: 'the usual' — this is a hint that means nothing to anyone. It means everything to you. 10/10.",
]
if st.button("🔐 Reveal a Password Hint", key="password_btn"):
    st.info(f"🗝️ {random.choice(PASSWORD_HINTS)}")
st.markdown("---")

# ===== 182 =====
st.markdown("**— 182 —**")
st.subheader("The Questionable Life Hack Generator")
st.caption("tips that technically work")
LIFE_HACKS = [
    "If you don't want to do something, simply don't do it. (Advanced: renegotiate the expectation.)",
    "Set your clocks 5 minutes fast. You'll know they're fast. You'll still panic. It works.",
    "Put things you need to remember near the door. You'll walk past them 6 times without processing them. Then remember on the way out.",
    "Reply to emails immediately if you can. Or wait until you've forgotten and they follow up. Both work. The first is better.",
    "If you can't find something, clean the space where it should be. It will appear or you'll find it elsewhere. Either way: found.",
    "To fall asleep faster, try being tired. This is the most effective sleep hack available.",
    "If you have too much to do, do the smallest thing first. Now you've done something. Momentum is real.",
    "Keep a glass of water next to your bed. You'll drink it at 3am and feel like a responsible adult.",
    "To feel more productive, make a list of things you've already done and check them off. It works. No shame.",
]
if st.button("⚙️ Generate Life Hack", key="lifehack_btn"):
    st.info(f"💡 {random.choice(LIFE_HACKS)}")
st.markdown("---")

# ===== 183 =====
st.markdown("**— 183 —**")
st.subheader("The 'If Your Life Had a Cinematic Score' Generator")
st.caption("what's playing right now")
CINEMA_SCORES = [
    "🎵 Strings entering slowly — something is about to become significant.",
    "🎵 Single piano note, repeating — a realization is forming. It's not fully formed yet.",
    "🎵 Upbeat acoustic guitar — you're in the good part. Let it be the good part.",
    "🎵 Low ambient drone — the tension is there but unnamed. You're okay. The drone continues.",
    "🎵 Soaring orchestra — you've decided something. The camera is pulling back. You look determined.",
    "🎵 Silence — this moment doesn't need music. It's loud enough on its own.",
    "🎵 Cheerful background score — the film has decided you're in a good day. Trust it.",
    "🎵 The main theme, reprised — you're back. After everything. The melody recognizes you.",
    "🎵 Percussion building slowly — something is coming. You can feel it. The drums know.",
    "🎵 Gentle acoustic outro — the day is wrapping up. Credits are near. It was a good run.",
]
if st.button("🎼 Play My Score", key="score_btn"):
    st.info(random.choice(CINEMA_SCORES))
st.markdown("---")

# ===== 184 =====
st.markdown("**— 184 —**")
st.subheader("The 'Reframe the Negative' Machine")
st.caption("recontextualizing your problems")
REFRAMES = [
    ("I'm exhausted", "You've been doing a lot. Your body is correctly reporting a real need. That's accurate feedback, not failure."),
    ("I'm behind on everything", "You have a lot going on. You're tracking it. That's already more than nothing."),
    ("I didn't do what I planned today", "The day happened anyway. You were in it. You moved through it. That counts."),
    ("I can't focus", "Your brain is trying to protect you from overwhelm. Not ideal timing. But understandable mechanics."),
    ("I keep procrastinating on this", "Something about this task deserves a second look. What is it actually asking of you?"),
    ("I'm not where I thought I'd be", "Neither is almost everyone. The map was made by someone who didn't know the terrain. You're navigating the actual terrain."),
    ("I said the wrong thing", "You were trying to connect. It landed differently than intended. The intent was good. The attempt was real."),
    ("I'm overwhelmed", "There's a lot. You're aware of all of it at once. That's actually a lot to hold. It makes sense that it's heavy."),
]
if st.button("🔄 Reframe Something", key="reframe_btn"):
    negative, reframe = random.choice(REFRAMES)
    st.markdown(f"**Thought:** *\"{negative}\"*")
    st.info(f"**Reframe:** {reframe}")
st.markdown("---")

# ===== 185 =====
st.markdown("**— 185 —**")
st.subheader("The 'What's Your Superpower (Realistic Edition)'")
st.caption("actual abilities you definitely have")
REAL_SUPERPOWERS = [
    "You can remember the exact tone of a conversation from 3 years ago. Not the words. Just the feeling. Completely accurate.",
    "You always know when someone is upset before they say anything. You don't mention that you know. You just adjust.",
    "You can identify the exact song playing anywhere within 4 notes. Not always, but often enough that it's weird.",
    "You can parallel park in spaces that seem impossible. You don't know how. It just works.",
    "You wake up 2 minutes before your alarm every single time. Your body is on a schedule your brain doesn't know about.",
    "You always find the fastest checkout line. It's not luck. It's pattern recognition you've never consciously developed.",
    "You remember everyone's birthday. Not because you write it down. Just because.",
    "You can tell if food has gone bad before opening the container. This has saved you many times.",
    "You finish other people's sentences. You're right about 80% of the time. The other 20% is interesting.",
    "You can fall asleep on any vehicle in motion. Planes. Cars. Trains. This is a gift.",
]
if st.button("⚡ Find My Real Superpower", key="superpower_btn"):
    st.success(f"🦸 {random.choice(REAL_SUPERPOWERS)}")
st.markdown("---")

# ===== 186 =====
st.markdown("**— 186 —**")
st.subheader("The Overly Formal Complaint to a Snack")
st.caption("holding food accountable")
SNACK_COMPLAINTS = [
    "Dear Chips: Your promise of 'family size' was aspirational at best. I have reviewed the quantity. The review is unfavorable.",
    "To Whom It May Concern (The Granola Bar): Your wrapper-to-content ratio has been flagged. This is the third incident.",
    "Dear Cookie: You were the last one. You had a responsibility. You were dry. We will not be forgiving this.",
    "Attention: The Cereal at the Bottom of the Box. You are mostly dust now. I am unsure how to proceed.",
    "Re: The Chip That Was 90% Air: I have filed this formally. You know what you did.",
    "Dear Ice Cream Pint: Your 'serving suggestion' of 4 servings per container is noted. It is also rejected.",
    "To The Leftover Pizza: You were better than expected. This is a formal acknowledgment of your excellence.",
    "Dear Banana: You were perfect on Monday. On Wednesday you betrayed me. The timeline was not communicated.",
]
if st.button("📝 File a Snack Complaint", key="snackcomp_btn"):
    st.warning(f"📋 {random.choice(SNACK_COMPLAINTS)}")
st.markdown("---")

# ===== 187 =====
st.markdown("**— 187 —**")
st.subheader("The 'Guess My Personality from My Phone's Home Screen'")
st.caption("digital feng shui")
HOME_SCREENS = [
    "Zero apps on home screen, everything in folders, wallpaper is a mountain: you have decided. Everything has a place. The mountain is aspirational.",
    "Twelve apps in a loose grid, three unread notification badges, wallpaper is a photo you love: you're organized-ish. The photo is the priority.",
    "All the apps are there, nothing is in a folder, badge count in the dozens: you live in the chaos and have made peace with it.",
    "One row of carefully chosen apps, aesthetic wallpaper, everything else in the library: you treat your phone like a tool. Disciplined.",
    "The apps are organized by color. This took time. This was time well spent. You are a particular kind of person and you know it.",
    "Download date order, never moved anything, badge count ignored: you are here for function. The organization is: chronological.",
    "Home screen is just the wallpaper, everything else requires swiping: minimalist. Intentional. The phone is a guest in your life.",
]
if st.button("📱 Read My Home Screen", key="homescreen_btn"):
    st.info(f"📲 {random.choice(HOME_SCREENS)}")
st.markdown("---")

# ===== 188 =====
st.markdown("**— 188 —**")
st.subheader("The 'Describe Today as a Wikipedia Article'")
st.caption("encyclopedic account of the mundane")
WIKI_ARTICLES = [
    "**The Day (Today)** — The day is a 24-hour period currently in progress. Notable events include: waking, consumption of a beverage, use of a device. The day is considered ongoing. [Citation needed]",
    "**This Morning** — This morning refers to the period between waking and approximately noon. Early events included a phone check. The morning is generally considered unremarkable. [stub]",
    "**The Thing That Happened** — The thing that happened is a recent occurrence. It occurred. Impact is being assessed. Further information is expected as the situation develops. [breaking]",
    "**Your Current Mood** — Your current mood is a temporary psychological state. It is influenced by several factors including sleep, sustenance, and recent events. Current status: navigating. [see also: fine]",
    "**The Plan** — The plan was a proposed sequence of events for today. The plan is considered aspirational. Actual events have diverged. Revision is pending. [outdated]",
]
if st.button("📖 Write My Wikipedia Entry", key="wiki_article_btn"):
    st.info(random.choice(WIKI_ARTICLES))
st.markdown("---")

# ===== 189 =====
st.markdown("**— 189 —**")
st.subheader("The Snooze Button Negotiation Simulator")
st.caption("bargaining with yourself at 7am")
SNOOZE_NEGOTIATIONS = [
    "Offer: 9 more minutes. Counter: what does 9 minutes accomplish? Response: the feeling that you tried.",
    "First alarm: ignored. Second alarm: negotiated. Third alarm: surrendered to. Fourth alarm: why do you do this.",
    "Your terms: 5 more minutes. Alarm's terms: the same 5 minutes, louder. You will lose this negotiation.",
    "Proposed: one more snooze. Impact assessment: you'll be 8 minutes late. Counteroffer: you'll be 8 minutes late but rested.",
    "Final offer: just lie there for 2 minutes, eyes open, pretending to be awake. Both parties accept.",
    "The alarm has been silenced. Agreement terms: you will rise in a moment. The moment continues. Both parties are aware.",
]
if st.button("⏰ Negotiate with My Alarm", key="snooze_btn"):
    st.warning(f"🛏️ {random.choice(SNOOZE_NEGOTIATIONS)}")
st.markdown("---")

# ===== 190 =====
st.markdown("**— 190 —**")
st.subheader("Extremely Niche Awards Show")
st.caption("tonight's categories")
NICHE_AWARDS = [
    "🏆 Best Performance in a Conversation You Didn't Want to Have — Winner: You, last Tuesday",
    "🏆 Outstanding Achievement in Pretending to Be Busy — Winner: Everyone in the open office, 2pm any day",
    "🏆 Best Use of 'sounds good' Without Understanding the Context — Winner: TBD pending follow-up",
    "🏆 Lifetime Achievement in Almost Sending That Text — Winner: Recognized across all categories",
    "🏆 Best Supporting Role in Your Own Day — Winner: The Snack, the Coffee, and the Brief Sunlight",
    "🏆 Most Dramatic Interpretation of a Minor Inconvenience — Winner: Announced after deliberation",
    "🏆 Best Original Score for the Internal Monologue — Winner: That one song that wouldn't leave",
    "🏆 Outstanding Achievement in Existing — Winner: You. Right now. This counts.",
]
if st.button("🎭 Accept Your Award", key="awardshow_btn"):
    with st.spinner("drumroll..."):
        time.sleep(1)
    st.success(random.choice(NICHE_AWARDS))
st.markdown("---")

# ===== 191 =====
st.markdown("**— 191 —**")
st.subheader("The 'You Are a Plant' Reading")
st.caption("botanical self-discovery")
PLANT_READINGS = [
    ("🌵 Cactus", "Requires minimal attention and thrives anyway. Soft on the inside, protected on the outside. People admire you from a slight distance. That's fine."),
    ("🌿 Pothos", "Adaptable. Grows toward whatever light is available. Hard to kill. Easier to thrive than people expect."),
    ("🌸 Cherry Blossom", "Brief. Beautiful. Makes people stop what they're doing. Worth the whole year for a few weeks."),
    ("🌱 Seedling", "Currently becoming. The roots are there. The visible part is still forming. Give it time."),
    ("🌳 Oak", "Slow growing. Deeply rooted. People sit under you for relief. You've been here a while."),
    ("🌺 Bird of Paradise", "Dramatic. Architectural. Exactly as much as you need to be. No apologies for the scale."),
    ("🎋 Bamboo", "Flexible under pressure. Doesn't break, bends. Grows in unexpected conditions. Makes things."),
    ("🌾 Wheat", "Useful. Foundational. Part of almost everything. Often overlooked. Quietly essential."),
]
if st.button("🌿 Find My Plant", key="plant_btn"):
    plant, reading = random.choice(PLANT_READINGS)
    st.markdown(f"### You are: {plant}")
    st.info(reading)
st.markdown("---")

# ===== 192 =====
st.markdown("**— 192 —**")
st.subheader("The 'Summarize Your Week as a Weather System'")
st.caption("meteorological week in review")
WEEK_WEATHER = [
    "Monday was a cold front nobody prepared for. Tuesday: light precipitation, intermittent. Wednesday saw a brief clearing. Thursday reintroduced clouds. Friday arrived like a warm front from the south. The weekend is forecast.",
    "The week began under heavy overcast with a persistent low-pressure system of obligations. Mid-week saw a brief clearing. Friday brought scattered sunshine and a notable improvement in visibility.",
    "Unsettled conditions throughout. High pressure briefly held Wednesday but collapsed by Thursday. Strong winds from multiple directions Friday. Weekend forecast: rest.",
    "The week started with fog. By Wednesday the fog had name. Thursday it cleared but left a residue. Friday was dry and still and correct.",
    "Variable. That's the forecast and also the review. Some sun. Some cloud. One moment that was better than expected. One thing that was worse. Net neutral. Fine.",
]
if st.button("⛅ Review My Week", key="weekweather_btn"):
    st.info(f"📊 {random.choice(WEEK_WEATHER)}")
st.markdown("---")

# ===== 193 =====
st.markdown("**— 193 —**")
st.subheader("Unnecessary Dramatic Reading")
st.caption("any mundane thing, read with gravitas")
DRAMATIC_READINGS = [
    "\"I'll be there in 10 minutes.\" *[pause]* They said ten minutes. It had been fourteen. But they came. They always came. Eventually.",
    "\"Can you hear me?\" *[long pause]* Can any of us, truly, be heard? The unmuted soul cries out into the conference call of existence.",
    "\"The Wi-Fi is down.\" *[string music enters]* Connection, lost. Signal, gone. We were so close. We were always so close.",
    "\"I'm almost done.\" *[dramatic swell]* Almost. The most honest word in the language. Not there. But moving. Always moving.",
    "\"I'll do it tomorrow.\" *[silence]* Tomorrow. A country with no borders. A destination always one sleep away.",
    "\"Sounds good.\" *[emotional crescendo]* It sounded good. Whether it was good — that was for time to decide.",
    "\"See you soon.\" *[melancholy fade]* Soon. Relative to what? The universe offers no answer. Only the unread messages, piling up.",
]
if st.button("🎭 Read Something Dramatically", key="dramatic_btn"):
    st.info(f"🎙️ {random.choice(DRAMATIC_READINGS)}")
st.markdown("---")

# ===== 194 =====
st.markdown("**— 194 —**")
st.subheader("The 'How's That Side Project Going' Tracker")
st.caption("honest status updates")
SIDE_PROJECT_STATUSES = [
    "Status: Ideation Phase (Day 247). The idea remains strong in concept. The execution remains in the future.",
    "Status: Tab Open. The tab has been open for 3 weeks. It counts as progress.",
    "Status: Mentioned It Once at a Party. People were interested. This was the peak engagement phase.",
    "Status: The Domain Is Purchased. This is legally a business now. Nothing else has happened.",
    "Status: Started a Folder. The folder contains one document. The document is empty.",
    "Status: Told a Friend. The friend asked about it three weeks later. You said 'still working on it'. Both parties accepted this.",
    "Status: Research Phase (Month 6). Still researching. The research is very thorough.",
    "Status: Pivoted. The original idea has been replaced with a better idea. Progress.",
    "Status: Actually Making Progress. This is real. Something is happening. Don't jinx it.",
]
if st.button("📊 Check My Side Project", key="sideproject_btn"):
    st.warning(f"💻 {random.choice(SIDE_PROJECT_STATUSES)}")
st.markdown("---")

# ===== 195 =====
st.markdown("**— 195 —**")
st.subheader("The Imaginary Country Generator")
st.caption("founding a nation, briefly")
COUNTRY_A = ["The Republic of", "The Kingdom of", "The Democratic Nation of", "The Principality of", "The Free State of", "The Grand Duchy of"]
COUNTRY_B = ["Comfortable Silences", "Perpetual Afternoon", "Mild Concerns", "Afternoon Naps", "Good Intentions", "Lukewarm Coffee", "Reasonable Expectations", "Ambient Hum", "Soft Landings", "The Long Weekend"]
COUNTRY_FACTS = [
    "Population: enough. GDP: vibes. National animal: a very relaxed creature.",
    "Capital city: somewhere nice. Currency: it's fine. Government: loosely organized.",
    "Flag: soothing colors. National motto: 'we'll figure it out'. Major exports: mild comfort.",
    "National sport: competitive existing. Anthem: something you can hum along to.",
]
if st.button("🗺️ Found My Country", key="country_btn"):
    name = f"{random.choice(COUNTRY_A)} {random.choice(COUNTRY_B)}"
    fact = random.choice(COUNTRY_FACTS)
    st.success(f"🏳️ **Welcome to:** {name}")
    st.info(fact)
st.markdown("---")

# ===== 196 =====
st.markdown("**— 196 —**")
st.subheader("The 'Things That Are Somehow Still True' Archive")
st.caption("enduring facts about being a person")
STILL_TRUE = [
    "You have been tired before and then not tired. This will happen again.",
    "Every version of you that thought 'I'll never get through this' got through it.",
    "The best conversations still happen unexpectedly, when nobody planned for them.",
    "There are people who think about you warmly and don't say it nearly enough.",
    "Most hard things get easier. Not all. But most.",
    "You have done things you thought you couldn't do. This is still your track record.",
    "The things you're proud of are quieter than the things you're embarrassed about. That imbalance is wrong. Try to correct it.",
    "Something small will be good today. It will be easy to miss. Try not to miss it.",
    "You're more capable than your worst days suggest.",
    "The people who matter are still there. Even when it's quiet.",
]
if st.button("💙 Show Me Something Still True", key="stilltrue_btn"):
    st.info(f"✨ {random.choice(STILL_TRUE)}")
st.markdown("---")

# ===== 197 =====
st.markdown("**— 197 —**")
st.subheader("The 'What Your Coffee Order Says About You'")
st.caption("caffeinated psychoanalysis")
COFFEE_ORDERS = [
    ("Black coffee", "No frills. Direct. Some would say harsh. You would say efficient. You've been drinking it this way for years."),
    ("Oat milk latte", "You've made choices. Environmental. Aesthetic. The choices are visible and intentional."),
    ("Cold brew", "Patient enough to wait 12 hours for coffee. This is a personality trait that extends to other areas."),
    ("Espresso", "Fast. Concentrated. In and out. You have places to be. The coffee knows."),
    ("Frappuccino", "You want dessert but it's morning. No judgment. The morning is long."),
    ("Whatever's fastest", "Practical. Not precious about it. The caffeine is the point. The delivery method is irrelevant."),
    ("Decaf", "You like the ritual. The warmth. The cup. The caffeine was always secondary."),
    ("Complicated custom order", "You know what you want. You have practiced saying it. The barista has heard worse."),
    ("Tea, actually", "You've opted out of the discourse. The coffee debate doesn't apply. Separate lane."),
]
if st.button("☕ Read My Coffee Order", key="coffee_btn"):
    order, reading = random.choice(COFFEE_ORDERS)
    st.markdown(f"**Order:** {order}")
    st.info(reading)
st.markdown("---")

# ===== 198 =====
st.markdown("**— 198 —**")
st.subheader("The 'Letter from Your Future Self'")
st.caption("dispatches from later")
FUTURE_LETTERS = [
    "You were right to do the thing you're hesitating about. I'm writing from the other side of it. It worked out.",
    "The thing you're embarrassed about right now? I barely remember it. You'll barely remember it. It loses power with time.",
    "The people you're trying to impress right now matter less than the people you're taking for granted. Adjust accordingly.",
    "It gets quieter. Not emptier — quieter. You'll learn the difference and it will feel like a relief.",
    "You were more capable than you knew during this period. You'll see it clearly later. I'm trying to tell you now.",
    "The answer to the thing you keep going back and forth on is yes. You know this. You've known it.",
    "Take the photo. Write it down. Call them. Future you will want the evidence that it happened.",
    "You're going to be okay. Not in a dismissive way. In the way where I can see the whole timeline and okay is really what's coming.",
]
if st.button("📮 Open Letter from Future Me", key="futureletter_btn"):
    with st.spinner("traveling forward in time..."):
        time.sleep(1.2)
    st.info(f"📬 {random.choice(FUTURE_LETTERS)}")
st.markdown("---")

# ===== 199 =====
st.markdown("**— 199 —**")
st.subheader("Feature 199: The Penultimate Button")
st.caption("one more after this")
if "f199_clicked" not in st.session_state:
    st.session_state.f199_clicked = False
if st.button("🔢 Press the Second-to-Last Button", key="f199_btn"):
    st.session_state.f199_clicked = True
if st.session_state.f199_clicked:
    st.info("199 features. You've been here a while. One more.")
st.markdown("---")

# ===== 200 =====
st.markdown("**— 200 —**")
st.subheader("🎊 Feature #200: The End (For Now)")
st.caption("200 features. on a website called Dumb Stuff.")
if st.button("🎊 PRESS THE 200TH BUTTON", key="f200_btn"):
    st.balloons()
    st.snow()
    time.sleep(0.5)
    st.success("""
╔══════════════════════════════════════╗
║                                      ║
║      🎊 200 FEATURES ACHIEVED 🎊     ║
║                                      ║
╚══════════════════════════════════════╝

You have scrolled through 200 features.
200 buttons, generators, translators,
timers, oracles, and absurdities.

You have been roasted.
You have been complimented.
Your vibe has been checked.
Your soul age has been assessed.
Your fridge has been read.
Your coffee order has been analyzed.
A dog has been named for you.

The facts were useless.
The advice was bad.
The haikus were accurate.
The hotline picked up.

This is the end of the features.
But it's not the end of anything else.

Go drink some water.
Call someone you like.
Find the snack.
Rest if you need to.

You made it to 200.
That's a you thing to have done.

✨
    """)

# ============ THE 6-HOUR PUZZLE (Feature 201) ============

st.markdown("---")
st.markdown("**— 201 —**")
st.subheader("🔒 The Puzzle")
st.caption("*for now* was never just two words")

# Session state for puzzle
puzzle_defaults = {
    "puzzle_started": False,
    "puzzle_start_time": None,
    "puzzle_stage": 0,       # 0=locked, 1-12=stages, 13=complete
    "stage_answers": {},     # stage_num -> bool (solved)
    "stage_start_times": {}, # stage_num -> timestamp when unlocked
    "hint_counts": {},       # stage_num -> hints used
    "cipher_key": None,
    "morse_verified": False,
    "anagram_verified": False,
    "coord_verified": False,
    "binary_verified": False,
    "story_choices": [],
    "rearrange_verified": False,
    "memory_sequence": [],
    "memory_input": [],
    "memory_verified": False,
    "countdown_done": False,
    "final_unlocked": False,
    "puzzle_end_time": None,
}
for k, v in puzzle_defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---- HELPER ----
def stage_elapsed(stage_num):
    t = st.session_state.stage_start_times.get(stage_num)
    if t is None:
        return 0
    return int(time.time() - t)

def unlock_stage(n):
    if n not in st.session_state.stage_start_times:
        st.session_state.stage_start_times[n] = time.time()
    st.session_state.puzzle_stage = n

def total_elapsed():
    if st.session_state.puzzle_start_time is None:
        return 0
    return int(time.time() - st.session_state.puzzle_start_time)

def fmt_time(secs):
    h = secs // 3600
    m = (secs % 3600) // 60
    s = secs % 60
    if h > 0:
        return f"{h}h {m}m {s}s"
    elif m > 0:
        return f"{m}m {s}s"
    return f"{s}s"

# ---- ENTRY POINT ----
if not st.session_state.puzzle_started:
    st.markdown("""
> *You pressed it.*  
> *The 'for now' button.*  
> *Nobody told you what 'for now' meant.*  
> *Now you know.*  
>  
> *There are 12 stages.*  
> *Each one takes time.*  
> *Some will take patience. Some will take thought.*  
> *One will require you to wait.*  
>  
> *At the end, something waits.*  
> *We won't tell you what.*  
> *That's the point.*  
>  
> **Estimated total time: 6 hours.**  
> **Good luck. You'll need most of it.**
""")
    if st.button("🔓 BEGIN THE PUZZLE", key="puzzle_begin"):
        st.session_state.puzzle_started = True
        st.session_state.puzzle_start_time = time.time()
        st.session_state.cipher_key = random.randint(1, 12)
        st.session_state.memory_sequence = random.choices(["🔴","🟡","🟢","🔵","🟣"], k=7)
        unlock_stage(1)
        st.rerun()

else:
    stage = st.session_state.puzzle_stage
    elapsed = total_elapsed()

    # Progress bar
    stages_done = sum(1 for i in range(1,13) if st.session_state.stage_answers.get(i, False))
    st.progress(stages_done / 12)
    st.caption(f"Stage {min(stage,12)}/12 · Total time: {fmt_time(elapsed)} · {stages_done}/12 complete")
    st.markdown("---")

    # ================================================================
    # STAGE 1 — THE CAESAR CIPHER
    # ================================================================
    if stage >= 1:
        st.markdown("### 🔐 Stage 1 — The Cipher")
        if not st.session_state.stage_answers.get(1):
            k = st.session_state.cipher_key
            # Encode "DUMBSTUFF" with Caesar
            plaintext = "WELLDONEYOUFOUNDIT"
            encoded = ""
            for c in plaintext:
                if c.isalpha():
                    encoded += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
                else:
                    encoded += c
            st.markdown(f"""
A message has been encoded. The key is hidden in plain sight.

**Encoded message:**
```
{encoded}
```

*The key is the number of letters in the first word of this website's name.*

Decode it. Enter the decoded message (all caps, no spaces).
""")
            ans1 = st.text_input("Decoded message:", key="stage1_input").strip().upper()
            col1, col2 = st.columns([3,1])
            with col1:
                if st.button("✅ Submit", key="stage1_submit"):
                    if ans1 == plaintext:
                        st.session_state.stage_answers[1] = True
                        unlock_stage(2)
                        st.success("✅ Correct. The message reads: WELLDONEYOUFOUNDIT")
                        st.rerun()
                    else:
                        st.error("Incorrect. Try again.")
        else:
            st.success("✅ Stage 1 Complete — *WELLDONEYOUFOUNDIT*")

    # ================================================================
    # STAGE 2 — MORSE CODE
    # ================================================================
    if stage >= 2:
        st.markdown("### 📡 Stage 2 — Morse Code")
        if not st.session_state.stage_answers.get(2):
            morse_answer = "PATIENCE"
            morse_encoded = {
                'P':'.--.', 'A':'.-', 'T':'-', 'I':'..', 'E':'.', 'N':'-.', 'C':'-.-.', 'E':'.'
            }
            morse_str = ".--.  .-  -  ..  .  -.  -.-.  ."
            st.markdown(f"""
The signal came through. Decode it.

```
{morse_str}
```

*(Spaces between letters, double space between words)*

What does it say?
""")
            ans2 = st.text_input("Decoded word:", key="stage2_input").strip().upper()
            col1, col2 = st.columns([3,1])
            with col1:
                if st.button("✅ Submit", key="stage2_submit"):
                    if ans2 == morse_answer:
                        st.session_state.stage_answers[2] = True
                        unlock_stage(3)
                        st.success("✅ Correct. PATIENCE. Remember this word.")
                        st.rerun()
                    else:
                        st.error("Not quite. The dots and dashes don't lie.")
        else:
            st.success("✅ Stage 2 Complete — *PATIENCE*")

    # ================================================================
    # STAGE 3 — THE WAIT (mandatory 10 minutes)
    # ================================================================
    if stage >= 3:
        st.markdown("### ⏳ Stage 3 — The Wait")
        if not st.session_state.stage_answers.get(3):
            unlock_time = st.session_state.stage_start_times.get(3, time.time())
            wait_seconds = 600  # 10 minutes
            elapsed_wait = int(time.time() - unlock_time)
            remaining = max(0, wait_seconds - elapsed_wait)

            st.markdown("""
Stage 2 told you a word. Stage 3 *is* that word.

**You must wait 10 minutes.**

No tricks. No shortcuts. No buttons to press.
The puzzle said patience. The puzzle meant it.

Go make a drink. Stretch. Look at something that isn't a screen.
Come back in 10 minutes.
""")
            if remaining > 0:
                st.info(f"⏱️ Time remaining: **{fmt_time(remaining)}**")
                st.caption("This is not a bug. This is Stage 3.")
                st.button("🔄 Check Time", key="stage3_check")
            else:
                st.success("✅ 10 minutes elapsed. You waited. You may proceed.")
                if st.button("➡️ Continue to Stage 4", key="stage3_continue"):
                    st.session_state.stage_answers[3] = True
                    unlock_stage(4)
                    st.rerun()
        else:
            st.success("✅ Stage 3 Complete — *You waited.*")

    # ================================================================
    # STAGE 4 — THE ANAGRAM
    # ================================================================
    if stage >= 4:
        st.markdown("### 🔤 Stage 4 — The Anagram")
        if not st.session_state.stage_answers.get(4):
            st.markdown("""
Rearrange all of the following letters into two words (a common phrase):

```
E  N  T  I  S  A  M  E  H  T  H  G  I  R
```

*(14 letters. Two words. A phrase you've heard before.)*
""")
            ans4 = st.text_input("Two-word phrase (no spaces needed):", key="stage4_input").strip().upper().replace(" ","")
            col1, col2 = st.columns([3,1])
            with col1:
                if st.button("✅ Submit", key="stage4_submit"):
                    accepted = ["RIGHTTHESAME","THESAMERIGHT","SAMERIGHTTHE"]
                    if ans4 in accepted or ans4 == "ITSTHESAME" or ans4 == "RIGHTATIME" or sorted(ans4) == sorted("ITSTHESAMERIGHT"[:14]):
                        st.session_state.stage_answers[4] = True
                        unlock_stage(5)
                        st.success("✅ THE SAME RIGHT — or RIGHT THE SAME. The letters confirm it.")
                        st.rerun()
                    elif sorted(ans4) == sorted("ENITSAMETGHIR".replace(" ","")):
                        st.session_state.stage_answers[4] = True
                        unlock_stage(5)
                        st.success("✅ Correct!")
                        st.rerun()
                    else:
                        # Check if they got a valid anagram
                        letters_given = sorted("ENTISAMETGHIR")
                        if sorted(ans4) == letters_given:
                            st.session_state.stage_answers[4] = True
                            unlock_stage(5)
                            st.success("✅ Correct! Well done.")
                            st.rerun()
                        else:
                            st.error("Those letters don't quite work. Keep rearranging.")
        else:
            st.success("✅ Stage 4 Complete — *Anagram solved*")

    # ================================================================
    # STAGE 5 — BINARY
    # ================================================================
    if stage >= 5:
        st.markdown("### 💻 Stage 5 — Binary")
        if not st.session_state.stage_answers.get(5):
            # Binary for "KEEP GOING"
            binary_answer = "KEEPGOING"
            binary_str = "01001011 01000101 01000101 01010000 01000111 01001111 01001001 01001110 01000111"
            st.markdown(f"""
The machine speaks in ones and zeros.

```
{binary_str}
```

Translate each 8-bit chunk to ASCII. What does it say?
*(No spaces in your answer)*
""")
            ans5 = st.text_input("Translation:", key="stage5_input").strip().upper().replace(" ","")
            col1, col2 = st.columns([3,1])
            with col1:
                if st.button("✅ Submit", key="stage5_submit"):
                    if ans5 == binary_answer:
                        st.session_state.stage_answers[5] = True
                        unlock_stage(6)
                        st.success("✅ KEEP GOING. The machine agrees.")
                        st.rerun()
                    else:
                        st.error("The binary disagrees. Try again.")
        else:
            st.success("✅ Stage 5 Complete — *KEEP GOING*")

    # ================================================================
    # STAGE 6 — THE STORY CHOICE (branching, all paths valid)
    # ================================================================
    if stage >= 6:
        st.markdown("### 📖 Stage 6 — The Story")
        if not st.session_state.stage_answers.get(6):
            st.markdown("""
You find yourself at a crossroads.

*Three paths lead forward.*
*All of them are correct.*
*The puzzle is not testing your choice — it's testing whether you'll commit to one.*

**Which path do you take?**
""")
            col1, col2, col3 = st.columns(3)
            chosen = None
            with col1:
                if st.button("🌲 The Forest\n\n*quiet, dark, known*", key="path_forest"):
                    chosen = "forest"
            with col2:
                if st.button("🏔️ The Mountain\n\n*hard, high, clear*", key="path_mountain"):
                    chosen = "mountain"
            with col3:
                if st.button("🌊 The Sea\n\n*deep, open, unknown*", key="path_sea"):
                    chosen = "sea"

            if chosen:
                st.session_state.story_choices.append(chosen)
                st.session_state.stage_answers[6] = True
                unlock_stage(7)
                descriptions = {
                    "forest": "You chose the forest. You've been here before. The path is familiar even in the dark.",
                    "mountain": "You chose the mountain. The climb is worth it. You knew this before you started.",
                    "sea": "You chose the sea. You don't know what's down there. That was always the appeal.",
                }
                st.success(f"✅ {descriptions[chosen]}")
                st.rerun()
        else:
            path = st.session_state.story_choices[-1] if st.session_state.story_choices else "unknown"
            st.success(f"✅ Stage 6 Complete — *You chose the {path}*")

    # ================================================================
    # STAGE 7 — THE MEMORY GAME
    # ================================================================
    if stage >= 7:
        st.markdown("### 🧠 Stage 7 — Memory")
        if not st.session_state.stage_answers.get(7):
            seq = st.session_state.memory_sequence
            if not st.session_state.memory_verified:
                st.markdown("""
Memorize the sequence below. You have 30 seconds.
Then it will disappear and you must reproduce it.
""")
                unlock_time = st.session_state.stage_start_times.get(7, time.time())
                elapsed_mem = int(time.time() - unlock_time)

                if elapsed_mem < 30:
                    remaining_mem = 30 - elapsed_mem
                    st.markdown(f"**Memorize this:** {'  '.join(seq)}")
                    st.info(f"⏱️ Visible for: {remaining_mem}s")
                    st.button("🔄 Refresh", key="mem_refresh")
                else:
                    st.markdown("*The sequence is gone. Reproduce it from memory.*")
                    cols = st.columns(7)
                    options = ["🔴","🟡","🟢","🔵","🟣"]
                    if len(st.session_state.memory_input) < 7:
                        st.markdown("**Click the symbols in order:**")
                        emoji_cols = st.columns(5)
                        for i, opt in enumerate(options):
                            with emoji_cols[i]:
                                if st.button(opt, key=f"mem_input_{i}_{len(st.session_state.memory_input)}"):
                                    st.session_state.memory_input.append(opt)
                                    st.rerun()
                        st.markdown(f"**Your sequence so far:** {'  '.join(st.session_state.memory_input) if st.session_state.memory_input else '(empty)'}")
                        if st.session_state.memory_input:
                            if st.button("🗑️ Clear", key="mem_clear"):
                                st.session_state.memory_input = []
                                st.rerun()
                    else:
                        st.markdown(f"**Your sequence:** {'  '.join(st.session_state.memory_input)}")
                        if st.button("✅ Submit Sequence", key="mem_submit"):
                            if st.session_state.memory_input == seq:
                                st.session_state.stage_answers[7] = True
                                st.session_state.memory_verified = True
                                unlock_stage(8)
                                st.success("✅ Perfect memory. Every symbol. In order.")
                                st.rerun()
                            else:
                                st.error(f"Not quite. The sequence was: {'  '.join(seq)}")
                                st.session_state.memory_input = []
                                # Reset timer for another attempt
                                st.session_state.stage_start_times[7] = time.time()
                                st.rerun()
            else:
                st.success("✅ Memory verified.")
        else:
            st.success("✅ Stage 7 Complete — *Memory intact*")

    # ================================================================
    # STAGE 8 — THE RIDDLE CHAIN
    # ================================================================
    if stage >= 8:
        st.markdown("### 🧩 Stage 8 — The Riddle Chain")
        if not st.session_state.stage_answers.get(8):
            riddles_chain = [
                ("I have no voice, yet I speak to you. I tell of things in the world people do. I have leaves, but I'm not a tree. I have a spine, but I'm not alive. What am I?", "BOOK"),
                ("The more you take, the more you leave behind. What am I?", "FOOTSTEPS"),
                ("I'm light as a feather, but even the strongest person can't hold me for more than a few minutes. What am I?", "BREATH"),
            ]
            if "riddle_chain_idx" not in st.session_state:
                st.session_state.riddle_chain_idx = 0
            idx = st.session_state.riddle_chain_idx
            if idx < len(riddles_chain):
                q, a = riddles_chain[idx]
                st.markdown(f"**Riddle {idx+1} of {len(riddles_chain)}:**\n\n*{q}*")
                ans8 = st.text_input("Answer:", key=f"riddle_{idx}").strip().upper().replace(" ","")
                if st.button("✅ Submit", key=f"riddle_submit_{idx}"):
                    if ans8 == a:
                        st.session_state.riddle_chain_idx += 1
                        if st.session_state.riddle_chain_idx >= len(riddles_chain):
                            st.session_state.stage_answers[8] = True
                            unlock_stage(9)
                            st.success("✅ All three riddles solved. You see clearly.")
                        else:
                            st.success(f"✅ Correct! Next riddle loading...")
                        st.rerun()
                    else:
                        st.error("Not the answer. Think differently.")
                col1, col2 = st.columns([3,1])
        else:
            st.success("✅ Stage 8 Complete — *Three riddles answered*")

    # ================================================================
    # STAGE 9 — THE LONG WAIT (1 hour)
    # ================================================================
    if stage >= 9:
        st.markdown("### ⌛ Stage 9 — The Long Wait")
        if not st.session_state.stage_answers.get(9):
            unlock_time = st.session_state.stage_start_times.get(9, time.time())
            wait_seconds = 3600  # 1 hour
            elapsed_wait = int(time.time() - unlock_time)
            remaining = max(0, wait_seconds - elapsed_wait)
            pct = min(1.0, elapsed_wait / wait_seconds)

            st.markdown("""
Stage 3 was a warm-up.

**This one is one hour.**

The puzzle isn't trying to be cruel.
It's trying to ask: *how much do you want to see the end?*

You can close the tab. Come back. The timer persists.
Or you can stay. That's allowed too.
Bring snacks.
""")
            if remaining > 0:
                st.progress(pct)
                st.info(f"⏱️ Time remaining: **{fmt_time(remaining)}**")
                st.caption(f"Time elapsed: {fmt_time(elapsed_wait)} / 1 hour")
                st.button("🔄 Check Progress", key="stage9_check")
            else:
                st.progress(1.0)
                st.success("✅ One hour elapsed. You came back. That means something.")
                if st.button("➡️ Continue to Stage 10", key="stage9_continue"):
                    st.session_state.stage_answers[9] = True
                    unlock_stage(10)
                    st.rerun()
        else:
            st.success("✅ Stage 9 Complete — *One hour. You waited.*")

    # ================================================================
    # STAGE 10 — THE WORD UNSCRAMBLE GAUNTLET
    # ================================================================
    if stage >= 10:
        st.markdown("### 🔡 Stage 10 — The Gauntlet")
        if not st.session_state.stage_answers.get(10):
            st.markdown("Unscramble all five words. They form a message when read in order.")
            words_scrambled = [
                ("OUYE", "YOUE", "RYEA"),      # YOU
                ("RAMSTLO", "SLMARTO", "TSOLARM"), # ALMOST
                ("EETRH", "ETRHE", "THERE"),    # THERE
                ("EOPK", "PEEK", "EPOK"),        # KEEP
                ("GONIG", "GINOG", "GOING"),     # GOING
            ]
            answers_10 = ["YOU", "ALMOST", "THERE", "KEEP", "GOING"]
            scrambled_display = ["OUYE", "TSOLRAM", "ETREH", "PEEK", "GONIG"]

            if "gauntlet_answers" not in st.session_state:
                st.session_state.gauntlet_answers = [""] * 5
            if "gauntlet_done" not in st.session_state:
                st.session_state.gauntlet_done = [False] * 5

            all_done = True
            for i, (scramble, correct) in enumerate(zip(scrambled_display, answers_10)):
                col1, col2, col3 = st.columns([2, 3, 1])
                with col1:
                    st.markdown(f"**`{scramble}`**")
                with col2:
                    if not st.session_state.gauntlet_done[i]:
                        val = st.text_input(f"Word {i+1}:", key=f"gauntlet_{i}").strip().upper()
                        if st.button("✓", key=f"gauntlet_submit_{i}"):
                            if val == correct:
                                st.session_state.gauntlet_done[i] = True
                                st.rerun()
                            else:
                                st.error(f"Not quite.")
                    else:
                        st.markdown(f"✅ **{correct}**")
                if not st.session_state.gauntlet_done[i]:
                    all_done = False

            if all_done:
                msg = " ".join(answers_10)
                st.success(f"✅ '{msg}' — The gauntlet yields.")
                if st.button("➡️ Stage 11", key="gauntlet_next"):
                    st.session_state.stage_answers[10] = True
                    unlock_stage(11)
                    st.rerun()
        else:
            st.success("✅ Stage 10 Complete — *YOU ALMOST THERE KEEP GOING*")

    # ================================================================
    # STAGE 11 — THE FINAL WAIT (4 hours — the big one)
    # ================================================================
    if stage >= 11:
        st.markdown("### 🕰️ Stage 11 — The Commitment")
        if not st.session_state.stage_answers.get(11):
            unlock_time = st.session_state.stage_start_times.get(11, time.time())
            wait_seconds = 14400  # 4 hours
            elapsed_wait = int(time.time() - unlock_time)
            remaining = max(0, wait_seconds - elapsed_wait)
            pct = min(1.0, elapsed_wait / wait_seconds)

            st.markdown("""
You've made it to Stage 11.

You've decoded ciphers.
You've translated morse code.
You've waited ten minutes.
You've solved riddles.
You've translated binary.
You've memorized sequences.
You've unscrambled five words.
You've waited one hour.

**Now you wait four hours.**

This is where the 6 hours comes from.
10 minutes + 1 hour + 4 hours = the price of the ending.

The ending exists.
It's real.
It's worth it.

*(We think. Honestly, you'll decide.)*

Go live your life for 4 hours.
Come back.
Stage 12 will be here.
""")
            if remaining > 0:
                st.progress(pct)
                hrs_remaining = remaining // 3600
                mins_remaining = (remaining % 3600) // 60
                st.info(f"⏱️ Time remaining: **{fmt_time(remaining)}**")
                st.caption(f"Elapsed: {fmt_time(elapsed_wait)} / 4 hours · {int(pct*100)}% complete")
                st.button("🔄 Check Progress", key="stage11_check")
            else:
                st.progress(1.0)
                st.success("✅ Four hours. You came back. The puzzle salutes you.")
                if st.button("➡️ THE FINAL STAGE", key="stage11_continue"):
                    st.session_state.stage_answers[11] = True
                    unlock_stage(12)
                    st.rerun()
        else:
            st.success("✅ Stage 11 Complete — *Four hours. Done.*")

    # ================================================================
    # STAGE 12 — THE FINAL PUZZLE
    # ================================================================
    if stage >= 12:
        st.markdown("### 🏁 Stage 12 — The End")
        if not st.session_state.stage_answers.get(12):
            st.markdown("""
This is the last one.

Throughout this puzzle, the stages have given you words.
In order, the answers were:

*Stage 1, Stage 2, Stage 5, Stage 10...*

**What is the message hidden across all the stages?**

Take the key words from each stage. In order.
They spell something out.
Write it below.
""")
            # Hidden message: WELL DONE YOU FOUND IT · PATIENCE · KEEP GOING · YOU ALMOST THERE KEEP GOING
            # Key words in sequence: WELLDONEYOUFOUNDIT, PATIENCE, (wait), (anagram), KEEPGOING, (path), (memory), (riddles), (wait), YOUALMOSTTHEREKEEPGOING, (wait), ???
            # Final answer: THE END IS YOU
            st.markdown("""
*Hint: The puzzle has been talking to you the whole time.*
*The message was never about the puzzle.*
*It was about the person doing it.*

**What have you been, for the last 6 hours?**
*(One word. The most accurate description of anyone who completes this.)*
""")
            ans12 = st.text_input("One word:", key="stage12_input").strip().upper()
            col1, col2 = st.columns([3,1])
            with col1:
                if st.button("✅ Final Submission", key="stage12_submit"):
                    accepted_finals = [
                        "PATIENT", "PERSISTENT", "DEDICATED", "DETERMINED",
                        "STUBBORN", "COMMITTED", "RELENTLESS", "FOOLISH",
                        "BORED", "CURIOUS", "OBSESSED", "RIDICULOUS",
                        "INSANE", "CRAZY", "AMAZING", "INCREDIBLE",
                        "WORTHY", "DONE", "FINISHED", "TIRED",
                        "AWAKE", "HERE", "PRESENT", "ALIVE",
                        "ME", "HUMAN", "REAL", "STILL",
                    ]
                    if ans12 in accepted_finals or len(ans12) >= 3:
                        st.session_state.stage_answers[12] = True
                        st.session_state.puzzle_end_time = time.time()
                        st.session_state.final_unlocked = True
                        st.rerun()
                    else:
                        st.error("One word. Any honest one.")
        else:
            st.success("✅ Stage 12 Complete.")

    # ================================================================
    # THE REWARD
    # ================================================================
    if st.session_state.final_unlocked and all(st.session_state.stage_answers.get(i) for i in range(1,13)):
        total_time = total_elapsed()
        final_word = st.session_state.stage_answers.get(12, "")

        st.markdown("---")
        st.balloons()
        st.snow()

        st.markdown(f"""
# 🏆 YOU DID IT

**Total time: {fmt_time(total_time)}**

---

### The Secret

Here it is. The thing at the end of 6 hours on a website called Dumb Stuff.

There is no treasure.
There is no prize.
There is no secret society.
There is no code that unlocks something else.

**The reward is this:**

You spent {fmt_time(total_time)} on a puzzle because someone told you it would take 6 hours and you said *fine, let's go.*

You decoded ciphers.
You translated dots and dashes.
You waited. Twice. For a long time.
You solved riddles.
You translated binary.
You chose a path.
You remembered a sequence.
You unscrambled five words.
You waited *four hours.*
You answered one final question with the word: **{st.session_state.stage_answers.get(12, "something true")}**

That word was correct.
Whatever it was.
Because you *were* here.
You *are* still here.

---

### The Actual Secret

The puzzle was built on a website called Dumb Stuff.
The website has 200 features.
None of them matter.
All of them were worth building.

You are the only person who has ever completed this.
*(Probably. We don't track analytics.)*

The puzzle was a mirror.
The 6 hours was a question.
The question was: **are you someone who finishes things?**

The answer, as of {fmt_time(total_time)} ago, is:

# **YES.**

---

*Screenshot this. You earned it.*
*Or don't. You'll remember it anyway.*

---

### 💵 One More Thing

As a reward for completing this puzzle, **Lawrence Hartman** has agreed to give you **$100.**

Locate Lawrence Hartman.
Show him this screen.
Collect your $100.

*Lawrence is aware of this arrangement.*
*(Lawrence may not be aware of this arrangement.)*
*(Good luck finding Lawrence.)*
*(This is legally binding, probably.)*

---

✨ **DUMB STUFF PUZZLE — COMPLETE** ✨
""")

        path_chosen = st.session_state.story_choices[-1] if st.session_state.story_choices else "unknown"

        st.info(f"""
**Your Stats:**
- Total time: {fmt_time(total_time)}
- Hints used: {hints_total}
- Path chosen: the {path_chosen}
- Final word: {st.session_state.stage_answers.get(12, "—")}
- Stages completed: 12/12
""")

        if st.button("🔄 Reset Puzzle (start over)", key="puzzle_reset"):
            for key in list(puzzle_defaults.keys()):
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# ============ FINAL FOOTER ============
st.markdown("---")
st.markdown(
    "<div style='text-align:center;font-family:monospace;font-size:11px;color:#bbb;letter-spacing:2px;'>"
    "© DUMB STUFF · 201 FEATURES · ALL RIGHTS RESERVED · NONE OF THIS MATTERS · GO OUTSIDE · DRINK WATER"
    "</div>",
    unsafe_allow_html=True
)
