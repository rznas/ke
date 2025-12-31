# Game Benchmarking Template

This folder contains templates for analyzing competitive games relevant to the Shahnameh: Legends of Persia project.

## Available Templates

1. **GAME_NAME.md** - Complete game benchmark template (manual fill)
2. **VIDEO_ANALYSIS_TEMPLATE.md** - Analyze individual YouTube videos
3. **YOUTUBE_ANALYSIS_GUIDE.md** - Guide for efficient video analysis
4. **CLAUDE_DEEP_RESEARCH_PROMPT.md** - AI-powered game research prompt ⭐
5. **FIND_GAMES_PROMPT.md** - AI-powered game discovery prompt ⭐ NEW

## How to Use These Templates

### Option 0: Discover Games First (Start Here!) ⭐⭐⭐

**If you don't know WHICH games to benchmark yet:**

1. Open `FIND_GAMES_PROMPT.md`
2. Copy the entire prompt (no customization needed!)
3. Paste into Claude Deep Research
4. Wait 30-60 minutes for comprehensive game discovery
5. Receive 35-45 game recommendations across all categories
6. Save to `docs/benchmarks/MASTER_GAME_LIST.md`
7. Use Tier 1 games for immediate analysis

**Time:** ~30-60 minutes
**Output:** Complete roadmap of what to benchmark
**Do this ONCE** at project start, update as needed

### Option 1: AI-Powered Research (Recommended) ⭐⭐

**Use Claude Deep Research for fast, comprehensive analysis:**

1. Open `CLAUDE_DEEP_RESEARCH_PROMPT.md`
2. Replace `[GAME_NAME]` with your target game
3. Copy the entire structured prompt
4. Paste into Claude Deep Research
5. Let Claude research and compile the analysis
6. Review, verify, and save output

**Time:** ~10-30 minutes (mostly Claude working)
**Best for:** Games with lots of public information
**Do this** for each game from your discovery list

### Option 2: Manual Analysis (Traditional)

1. **Copy the template:**
   ```bash
   cp _template/GAME_NAME.md ./[actual-game-name]/
   ```

2. **Rename the file:**
   - Use kebab-case: `hades.md`, `god-of-war-2018.md`, `ghost-of-tsushima.md`

3. **Fill out all sections:**
   - Replace all `[PLACEHOLDER]` text with actual information
   - Use "Unknown" or "N/A" for information you can't find
   - Add "TODO: Research" for sections to complete later

4. **Gather data from:**
   - Official game websites and developer interviews
   - Metacritic, OpenCritic, Steam reviews
   - YouTube gameplay and analysis videos
   - Reddit communities and fan wikis
   - GDC talks and postmortems (if available)
   - Sales data (VGChartz, SteamDB, public announcements)

5. **Focus on relevance:**
   - Prioritize sections most relevant to Shahnameh development
   - The "Key Takeaways" section is the most important
   - Link design decisions back to our project constraints (2-person team, free tools, episodic structure)

## Template Sections Explained

### Must-Have Sections
- **Game Overview:** Basic facts about the game
- **Business Model & Performance:** How it made money and succeeded
- **User Reception:** What players and critics thought
- **Core Gameplay Mechanics:** How it plays
- **Key Takeaways for Shahnameh:** What we learn (MOST IMPORTANT)

### Optional but Valuable
- **Cultural Representation:** Critical for games with cultural settings
- **Episodic/DLC Strategy:** Essential for games with episodic release
- **AI & Asset Creation:** Helpful for understanding production efficiency

### Quick Reference Section
Always fill this out first - it's a TL;DR for Claude Code agents

## Priority Games to Benchmark

Based on `docs/consultants/5_shahnameh_gdd.md`, prioritize analyzing:

### High Priority (Similar Genre/Style)
1. **Hades** - Roguelike action, Greek mythology, indie success
2. **God of War (2018)** - Third-person action, mythology, epic combat
3. **Ghost of Tsushima** - Historical action, cultural representation, combat design
4. **Dark Souls** - Combat design, difficulty, boss fights
5. **Prince of Persia series** - Persian setting, action-adventure

### Medium Priority (Specific Features)
6. **Assassin's Creed: Mirage** - Middle Eastern setting, historical action
7. **Hellblade: Senua's Sacrifice** - Small team, AAA-quality, narrative focus
8. **A Plague Tale: Innocence** - Small team, episodic feel, strong narrative
9. **Blasphemous** - 2D action, cultural mythology, indie production
10. **Sifu** - Melee combat, age/time mechanics, indie studio

### Lower Priority (Business Model / Marketing)
11. **Hitman (2016)** - Episodic release model
12. **Life is Strange** - Episodic narrative games
13. **The Walking Dead (Telltale)** - Episodic structure

## Analysis Tips

### For Combat-Focused Games
- Pay special attention to "game feel" - weight, impact, responsiveness
- Note UI feedback for hits, parries, dodges
- Document difficulty curve and learning curve
- Analyze boss fight design patterns

### For Narrative Games
- How is story delivered (cutscenes vs gameplay vs environmental)
- Character development techniques
- Player agency vs authored narrative balance
- Pacing between action and story

### For Indie/Small Team Games
- Asset reuse strategies
- Scope management
- Art style choices (stylized vs realistic)
- What they achieved vs what they cut

### For Cultural Games
- How they handled cultural authenticity
- Community reception from represented culture
- Consultation and research processes
- Balance between accuracy and gameplay

## Updating Existing Analyses

Benchmark documents should be living documents. Update when:
- New DLC or content releases
- Significant community sentiment shifts
- Post-launch data becomes available (sales, player counts)
- Developer postmortems or talks are published

Add updates to the "Update Log" section at the bottom.

## Integration with CLAUDE.md

All benchmark analyses are referenced in the main CLAUDE.md file. When adding a new game analysis:

1. Create the game folder and analysis file
2. Update CLAUDE.md's benchmark section with the game name and key learnings
3. Link specific design decisions in GDD to benchmark insights

## Quick Start Guide

**To analyze a new game:**

```bash
# 1. Create game folder
mkdir docs/benchmarks/hades

# 2. Copy template
cp docs/benchmarks/_template/GAME_NAME.md docs/benchmarks/hades/hades.md

# 3. Start with Quick Reference section
# 4. Fill out Business Model (important for episodic planning)
# 5. Complete Key Takeaways (most valuable section)
# 6. Fill remaining sections as time allows
```

**Minimum Viable Analysis:**
- Quick Reference (5 min)
- Business Model & Performance (15 min)
- User Reception (10 min)
- Key Takeaways for Shahnameh (20 min)

**Total: ~1 hour for actionable insights**

## Using Benchmarks During Development

### When Designing Combat
→ Reference: God of War, Dark Souls, Hades

### When Planning Episodic Structure
→ Reference: Hitman, Telltale games, Life is Strange

### When Creating Persian Setting
→ Reference: Prince of Persia, Assassin's Creed: Mirage, Ghost of Tsushima (for cultural handling)

### When Scoping for Small Team
→ Reference: Hellblade, A Plague Tale, Blasphemous

### When Pricing/Marketing
→ Reference: All indie success stories in benchmarks

## AI-Assisted Analysis

You can use Claude to help gather and analyze this information:

```
Prompt: "Analyze [GAME NAME] based on the template at docs/benchmarks/_template/GAME_NAME.md.
Focus on:
1. Combat mechanics relevant to a Dark Souls-inspired Persian mythology game
2. Business model insights for episodic release
3. What a 2-person team with AI tools could realistically adopt
4. Cultural representation best practices (if applicable)"
```

## Folder Structure

```
docs/benchmarks/
├── _template/                 # This folder
│   ├── README.md             # This file
│   └── GAME_NAME.md          # Template file
├── hades/
│   ├── hades.md              # Main analysis
│   └── screenshots/          # Visual references (optional)
├── god-of-war-2018/
│   └── god-of-war-2018.md
├── ghost-of-tsushima/
│   └── ghost-of-tsushima.md
└── ...
```

---

**Remember:** The goal is actionable insights, not comprehensive documentation. Focus on what helps Shahnameh development.
