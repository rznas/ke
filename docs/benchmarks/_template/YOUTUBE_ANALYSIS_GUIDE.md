# YouTube Video Analysis Guide

Many game analyses exist as YouTube videos rather than written articles. This guide helps extract maximum value from video sources for Shahnameh development.

---

## Why Analyze YouTube Videos?

**Advantages:**
- Visual demonstration of mechanics
- Real gameplay footage (not cherry-picked screenshots)
- Audio design examples
- Community commentary in comments
- Developer insights (GDC talks, dev diaries)
- Free and accessible
- Multiple perspectives on same game

**Types of Valuable Videos:**
1. **GDC Talks** - Developer postmortems and insights
2. **Reviews** - Professional critics (IGN, GameSpot, ACG)
3. **Analysis** - Deep dives (Game Maker's Toolkit, Razbuten)
4. **Gameplay** - Raw or commented playthroughs
5. **Speedruns** - Show game systems exploitation
6. **Retrospectives** - Long-term assessment

---

## Recommended YouTube Channels

### For Design Analysis
- **Game Maker's Toolkit** (Mark Brown) - Design deep dives
- **Noclip** - Developer documentaries
- **Design Doc** - Focused game design analysis
- **Adam Millard** - Architect of Games
- **Razbuten** - Player experience focus

### For Technical Analysis
- **Digital Foundry** - Technical performance
- **GDC** (Game Developers Conference) - Developer talks
- **IndieDev** - Small team development

### For Combat Analysis
- **Iron Pineapple** - Souls-like combat
- **GirlWithTheGreenHat** - Combat system breakdowns
- **Joseph Anderson** - Long-form critical analysis

### For Reviews
- **SkillUp** - In-depth reviews
- **ACG** (AngryCentaurGaming) - Detailed reviews
- **Mortismal Gaming** - 100% completion reviews
- **Gameranx** - Before You Buy series

### For Cultural Games
- **Story Mode** (PBS) - Cultural impact of games
- **Writing on Games** - Narrative and cultural analysis

---

## How to Analyze a Video Efficiently

### Pre-Watch Preparation (2 min)

1. **Check video metadata:**
   - Date (is it review of launch version or patched?)
   - Duration (worth the time investment?)
   - View count (popular opinion or niche?)
   - Channel credibility

2. **Scan comments:**
   - Timestamps (community-highlighted moments)
   - Disagreements (alternative perspectives)
   - Developer responses (official clarifications)

3. **Set your focus:**
   - What are you looking for? (Combat? Story? Scope?)
   - Which sections to watch vs skip

### During Watch (Active Analysis)

**Take Timestamps:**
```
[03:45] - Combat feels weighty, similar to Dark Souls
[12:30] - Boss design pattern: arena-based, 3 phases
[18:20] - Team was only 15 people - scope lesson
[24:10] - Art direction: stylized to hide technical limits
```

**Capture Quotes:**
> "The combat may look simple, but the depth comes from mastering spacing and timing, not memorizing 50-hit combos."
> - Timestamp: [08:15]

**Screenshot Key Moments:**
- UI examples
- Art style references
- Boss fight setups
- Environment designs

### Post-Watch Synthesis (10-20 min)

1. **Fill out video analysis template**
2. **Extract 3-5 actionable insights**
3. **Cross-reference with other sources**
4. **Add to main game benchmark document**

---

## Efficient Video Analysis Workflow

### Quick Analysis (30 minutes total)

**For:** Getting general sense of a game

1. **Watch (15-20 min):**
   - Play at 1.5x speed
   - Skip intro/outro
   - Focus on gameplay footage sections
   - Pause for key insights

2. **Document (10-15 min):**
   - Fill "Quick Summary" section
   - Note top 3 takeaways
   - Timestamp most valuable moments

### Deep Analysis (2-4 hours total)

**For:** Games very similar to Shahnameh

1. **Watch multiple videos (1-2 hours):**
   - Full review (30-60 min)
   - GDC talk if available (30-60 min)
   - Combat analysis (15-30 min)
   - Community response video (15-30 min)

2. **Document (1-2 hours):**
   - Complete video analysis template
   - Fill full game benchmark document
   - Create reference folder with screenshots
   - Cross-reference multiple sources

---

## Video Types & What to Extract

### 1. GDC Talks (30-60 min videos)

**Best For:** Development process insights

**What to Capture:**
- Team size and structure
- Development timeline
- Technical challenges and solutions
- Budget constraints and creative solutions
- Iteration process
- What they cut and why

**Example Search:**
- "[Game Name] GDC"
- "[Game Feature] postmortem"
- "[Developer Name] GDC talk"

**Key Channels:**
- GDC (official)
- Gaming Talks (unofficial compilation)

### 2. Review Videos (15-30 min)

**Best For:** Overall game assessment

**What to Capture:**
- Reviewer's score/verdict
- Praised features
- Criticized features
- Value proposition
- Target audience
- Comparison to similar games

**Example Searches:**
- "[Game Name] review"
- "[Game Name] worth it"
- "[Game Name] ACG review"

### 3. Analysis Videos (20-40 min)

**Best For:** Deep design insights

**What to Capture:**
- Specific mechanics breakdown
- Design patterns
- What makes feature work/not work
- Player psychology insights
- Comparison to genre conventions

**Example Searches:**
- "[Game Name] analysis"
- "[Game Name] combat breakdown"
- "Game Maker's Toolkit [Game Name]"

### 4. Gameplay Videos (30min - 4 hours)

**Best For:** Observing mechanics in action

**What to Watch For:**
- Combat flow and rhythm
- Enemy variety
- Boss fight patterns
- Environment traversal
- UI during gameplay
- Player decision-making

**Tip:** Watch at 2x speed, slow down for important moments

### 5. Developer Diaries/Behind-the-Scenes

**Best For:** Production process

**What to Capture:**
- Asset creation workflow
- Tool pipeline
- Team collaboration
- Challenges faced
- Why certain decisions were made

### 6. Retrospectives (40-90 min)

**Best For:** Long-term assessment

**What to Capture:**
- How opinion changed over time
- What aged well/poorly
- Post-launch content impact
- Community consensus
- Historical significance

---

## Analyzing Videos with Claude Code

### Method 1: Watch & Dictate

**While watching video:**
1. Keep Claude Code session open
2. Dictate key observations as you watch
3. Ask Claude to organize notes into template

**Prompt:**
```
I'm watching a review of [Game]. Here are my observations:
[paste your raw notes]

Organize these into the YouTube Video Analysis Template at
docs/benchmarks/_template/VIDEO_ANALYSIS_TEMPLATE.md
```

### Method 2: Timestamp Extraction

**Prompt:**
```
Watch [YouTube URL] and extract timestamps for:
- Combat mechanics demonstrations
- Boss fight examples
- Art style showcases
- Developer commentary on [specific feature]
- Mentions of team size or budget

Format as timestamp: description
```

**Note:** Claude can't actually watch videos, but you can describe what you see and ask for organization.

### Method 3: Multi-Source Synthesis

**After watching 3-4 videos on same game:**

**Prompt:**
```
I've watched these videos about [Game]:
1. [Video 1]: [Your notes]
2. [Video 2]: [Your notes]
3. [Video 3]: [Your notes]

Synthesize into key takeaways for Shahnameh development:
- Combat design lessons
- Scope insights for 2-person team
- Art direction ideas
```

---

## Creating Video Reference Collections

### Organized Playlists

**Create themed playlists:**

**Combat Design References:**
- God of War combat breakdown
- Dark Souls boss design analysis
- Hades build variety showcase

**Small Team Success Stories:**
- Hellblade: Senua's Sacrifice postmortem
- Stardew Valley one-person development
- Hollow Knight Team Cherry interview

**Cultural Representation:**
- Ghost of Tsushima cultural consultant interview
- Assassin's Creed Mirage Persian setting review
- Never Alone (Kisima Inŋitchuŋa) indigenous collaboration

**Persian Culture/Mythology:**
- Prince of Persia series retrospective
- Shahnameh reading/analysis videos
- Persian miniature painting tutorials
- Traditional Persian music performances

### Bookmark Structure

```
docs/benchmarks/[game-name]/
  ├── [game-name].md          # Main analysis
  ├── videos/
  │   ├── review.md           # Video analysis: main review
  │   ├── gdc-talk.md         # Video analysis: GDC talk
  │   └── combat-analysis.md  # Video analysis: combat breakdown
  └── screenshots/            # Captured moments
```

---

## Video Analysis Best Practices

### Do:
- ✅ Check video publish date (patches may have fixed issues)
- ✅ Read comments for alternative perspectives
- ✅ Watch multiple reviewers for balanced view
- ✅ Screenshot UI, combat, and art examples
- ✅ Note specific timestamps for reference
- ✅ Cross-reference with written reviews
- ✅ Consider reviewer bias (Souls-like fan reviewing Souls-like)

### Don't:
- ❌ Rely on a single video for complete picture
- ❌ Ignore video age (launch vs patched version)
- ❌ Skip checking comment corrections
- ❌ Take subjective opinions as objective facts
- ❌ Forget to verify claims (sales numbers, team size)
- ❌ Watch entire 4-hour playthrough for basic info

---

## Speed Watching Techniques

### 1.5x-2x Speed Watching

**Good for:**
- Reviews (talking heads)
- Retrospectives
- Analysis videos

**Not good for:**
- Combat demonstrations (need to see timing)
- Music showcases
- Audio design analysis

### Strategic Skipping

**Always Watch:**
- Conclusions/summaries
- Gameplay demonstrations
- Developer insights
- Comparison sections

**Usually Skip:**
- Long intros
- Sponsorship segments
- Unrelated tangents
- Extensive plot recaps (unless analyzing narrative)

### Chapter Markers

YouTube videos often have chapters. Jump to relevant sections:
- "Combat" chapter for mechanics
- "Verdict" for summary
- "Technical" for performance

---

## Common Video Sources by Game Type

### Action-Adventure (Shahnameh's genre)

**Priority Channels:**
- ACG
- SkillUp
- FightinCowboy (walkthroughs)

### Indie Success Analysis

**Priority Channels:**
- GDC
- Game Maker's Toolkit
- Noclip

### Cultural Games

**Priority Channels:**
- Writing on Games
- Jacob Geller
- Story Mode

---

## Example: Analyzing "God of War" via YouTube

### Video Selection (15 min)

**Must Watch:**
1. **GDC Talk:** "Raising Kratos: Making of God of War" (60 min)
   - Team size, budget, challenges

2. **Review:** "ACG Review" (15 min)
   - Overall assessment, value

3. **Combat:** "GirlWithTheGreenHat Combat Analysis" (20 min)
   - Mechanics breakdown

4. **Cultural:** "God of War and Norse Mythology" (30 min)
   - Cultural representation approach

**Optional:**
5. Speedrun (to see systems exploited)
6. Boss fight compilation
7. Retrospective after DLC

### Analysis Session (3 hours)

1. **Watch all videos (2 hours)**
   - Take timestamps
   - Capture quotes
   - Screenshot references

2. **Document (1 hour)**
   - Fill video analysis templates
   - Update main benchmark
   - Extract Shahnameh lessons

### Output

**Files Created:**
```
docs/benchmarks/god-of-war-2018/
  ├── god-of-war-2018.md      # Main benchmark
  ├── videos/
  │   ├── gdc-making-of.md    # GDC talk analysis
  │   ├── acg-review.md       # Review analysis
  │   └── combat-breakdown.md # Combat analysis
  └── screenshots/
      ├── combat-ui.png
      ├── boss-arena.png
      └── art-direction.png
```

---

## YouTube-Specific Tools

### Browser Extensions

**Video Speed Controller:**
- Fine-tune playback speed
- Keyboard shortcuts

**Video Note Taker:**
- Take timestamped notes directly

**Return YouTube Dislike:**
- See community sentiment (dislikes)

### YouTube Features

**Transcript:**
- Use auto-transcript to search for keywords
- Copy-paste relevant sections

**Chapters:**
- Jump to specific topics
- Create your own timestamps

**Playback Speed:**
- 1.25x for normal analysis
- 1.5x for known reviewers
- 0.75x for complex technical demos

---

## Video Analysis Workflow Summary

**Quick Flow (30 min per game):**
```
1. Find best review video (5 min search)
2. Watch at 1.5x (15-20 min)
3. Note top 3 takeaways (5 min)
4. Fill quick summary template (5 min)
```

**Deep Flow (3-4 hours per game):**
```
1. Find 4-5 videos (review, GDC, analysis, gameplay) (15 min)
2. Watch all, taking timestamps and notes (2-2.5 hours)
3. Capture screenshots of key moments (15 min)
4. Fill complete templates (1 hour)
5. Extract actionable insights (30 min)
```

---

## Storing Video References

### In Markdown Files

```markdown
**Primary Review:** [ACG - God of War](https://youtube.com/watch?v=XXXXX)
- Timestamp 08:15 - Combat weight discussion
- Timestamp 12:40 - Boss design praise
- Score: Buy
```

### In Benchmark Documents

Always include video sources in "References & Resources" section of main benchmark.

---

**Remember:** Videos are excellent for observing mechanics in action, but always cross-reference with multiple sources for accuracy. One reviewer's opinion isn't universal truth.
