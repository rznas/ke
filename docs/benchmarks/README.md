# Game Benchmarking & Competitive Analysis

**Purpose:** Analyze games relevant to Shahnameh: Legends of Persia to extract actionable design, business, and technical insights.

**Philosophy:** Learn from successful games while adapting to our constraints (2-person team, free AI tools, Persian cultural authenticity, episodic structure).

---

## Quick Access

### By Category

**Combat Design:**
- [God of War 2018](./god-of-war-2018/)
- [Dark Souls](./dark-souls/)
- [Hades](./hades/)

**Cultural Representation:**
- [Ghost of Tsushima](./ghost-of-tsushima/)
- Prince of Persia series (TODO)
- Assassin's Creed: Mirage (TODO)

**Small Team Success:**
- [Hellblade: Senua's Sacrifice](./hellblade/)
- A Plague Tale: Innocence (TODO)
- Blasphemous (TODO)

**Episodic Structure:**
- Hitman (2016) (TODO)
- Life is Strange (TODO)
- Telltale's The Walking Dead (TODO)

---

## Benchmark Status

| Game | Status | Priority | Key Focus Areas |
|------|--------|----------|----------------|
| **Hades** | 📝 Template Ready | HIGH | Roguelike progression, mythology, indie success |
| **God of War (2018)** | 📝 Template Ready | HIGH | Combat, mythology storytelling, AAA on focused scope |
| **Ghost of Tsushima** | 📝 Template Ready | HIGH | Cultural representation, samurai combat |
| **Dark Souls** | 📝 Template Ready | HIGH | Boss fights, difficulty, weighty combat |
| **Hellblade** | 📝 Template Ready | HIGH | Small team AAA quality, narrative focus |
| Prince of Persia | ⏳ TODO | MEDIUM | Persian setting, action-adventure |
| AC: Mirage | ⏳ TODO | MEDIUM | Middle Eastern setting, recent release |
| A Plague Tale | ⏳ TODO | MEDIUM | Small team, strong narrative |
| Blasphemous | ⏳ TODO | MEDIUM | 2D action, cultural mythology |
| Sifu | ⏳ TODO | MEDIUM | Melee combat, aging mechanics |
| Hitman (2016) | ⏳ TODO | LOW | Episodic business model |
| Life is Strange | ⏳ TODO | LOW | Episodic narrative |

---

## How to Use Benchmarks

### For Claude Code Agents

When working on specific features, reference relevant benchmarks:

**Example: Implementing Combat System**
```
Read benchmarks:
- docs/benchmarks/god-of-war-2018/god-of-war-2018.md (combat feel)
- docs/benchmarks/dark-souls/dark-souls.md (boss design)
- docs/benchmarks/hades/hades.md (progression)

Apply lessons to Shahnameh combat implementation.
```

### For Design Decisions

1. **Identify the design question** (e.g., "How should we handle difficulty?")
2. **Check relevant benchmarks** (Dark Souls, Hades, Hellblade)
3. **Extract lessons** (From "Key Takeaways" sections)
4. **Adapt to constraints** (2-person team, free tools)
5. **Document decision** (In `docs/consultants/`)

### For Scope Planning

Compare team sizes and budgets:
- **AAA games** → What NOT to attempt
- **Small team games** → What IS achievable
- **Indie successes** → Smart scope decisions

---

## Analysis Guidelines

### What to Capture

**Must Document:**
- Business model and pricing
- User reception (reviews, sales)
- Core mechanics that work/don't work
- Team size and development time
- Key takeaways for Shahnameh

**Nice to Have:**
- Technical implementation details
- Marketing strategies
- Post-launch support
- Community engagement

### Analysis Depth

**Quick Analysis (1 hour):**
- Business model
- User reviews
- Key features
- Main takeaways

**Deep Analysis (4-8 hours):**
- Complete template
- Detailed mechanics breakdown
- Cultural analysis
- Visual references

**Living Document:**
- Update as new data emerges
- Add post-launch insights
- Incorporate developer postmortems

---

## Key Insights Summary

### Combat Design Lessons

**From Dark Souls:**
- Weighty, deliberate combat > button mashing
- Boss fights as skill checks
- Difficulty as feature, not barrier
- Death as learning opportunity

**From God of War:**
- Camera importance for 3D melee
- Combo depth vs accessibility balance
- Environmental integration in combat
- Spectacle without sacrificing control

**From Hades:**
- Progression between runs (applies to episodic)
- Build variety for replayability
- Tight controls are paramount
- Difficulty options don't hurt "hardcore" appeal

### Cultural Representation Lessons

**From Ghost of Tsushima:**
- Extensive cultural research pays off
- Authenticity > stereotypes
- Consult community from represented culture
- Language and music are critical
- Visual beauty can be cultural strength

**From Assassin's Creed:**
- Historical consultants are valuable
- Balance accuracy with fun
- Discovery Tour concept (educational mode)
- Respectful portrayal wins community support

### Small Team Success Lessons

**From Hellblade:**
- Focused scope with AAA execution > broad scope
- Audio design can carry atmosphere (cheaper than visuals)
- Narrative focus can differentiate
- 20-person team CAN produce AAA feel
- 3 years with clear vision

**From A Plague Tale:**
- 40-person team, AA budget, AAA results
- Stealth over combat (easier to implement)
- Linear design allows polish
- Strong art direction > raw graphics

**From Blasphemous:**
- 2D can be epic (consider for Shahnameh?)
- Cultural mythology resonates globally
- Pixel art is cost-effective
- Tight combat in 2D is achievable

### Episodic Release Lessons

**From Hitman (2016):**
- Episodic can work for non-narrative games
- Monthly releases maintained interest
- Controversial at launch, accepted later
- Season pass model
- Each episode must be substantial

**From Telltale Games:**
- Episodic works best for narrative
- Cliffhangers maintain engagement
- 2-3 month gaps are acceptable
- All episodes should be planned upfront
- Technical debt compounds across episodes

**From Life is Strange:**
- Episodic built fanbase organically
- Community theorizing between episodes
- Budget-friendly for small teams
- Revenue from early episodes funds later ones

### Business Model Insights

**Premium Pricing ($20-60):**
- Works for strong IP or proven quality
- Requires marketing budget
- Review scores critical
- Word-of-mouth can carry indie games

**Episodic Pricing:**
- Shahnameh plan: $19.99, $19.99, $24.99
- Season pass discount (25% off total)
- Similar to Hitman model
- Lower barrier to entry (first episode)

**Free-to-Play:**
- NOT recommended for Shahnameh
- Requires ongoing content
- Monetization design complexity
- Community management overhead

### Technical Feasibility (2-Person + AI Team)

**Achievable from Benchmarks:**
- ✅ Focused combat system (Dark Souls depth)
- ✅ Strong narrative (Hellblade quality)
- ✅ Stylized visuals (Hades aesthetic)
- ✅ Cultural authenticity (Ghost of Tsushima approach)
- ✅ Episodic structure (Hitman model)
- ✅ 2-3 hours per episode (achievable scope)

**Out of Scope:**
- ❌ Open world (God of War scale)
- ❌ Multiplayer (any game)
- ❌ Live service (ongoing content)
- ❌ Massive enemy variety (focus on quality over quantity)
- ❌ Full voice acting in multiple languages (AI + free tools instead)

**Smart Compromises:**
- Use Hades' limited but polished environments over God of War's vast world
- Focus on boss quality (Dark Souls) over enemy quantity
- Stylized art (cheaper, ages better) over realistic (expensive, dates quickly)
- Linear/hub design over open world
- Episode structure allows iterative improvement

---

## Using AI for Benchmark Creation

### Step 0: Discover Games to Benchmark (START HERE) ⭐⭐⭐

**Before analyzing individual games, discover WHICH games to analyze:**

Use the game discovery prompt at `_template/FIND_GAMES_PROMPT.md`:

**What it does:**
- 🔍 Searches for 35-45 games across all categories
- 📊 Covers AAA blockbusters to tiny indie games
- 🎯 Prioritizes small team successes (most relevant to us)
- 📋 Creates 3-tier priority system (HIGH/MEDIUM/LOW)
- 🗺️ Provides strategic analysis roadmap
- ✅ Verifies research availability for each game

**Categories covered:**
1. AAA Combat Masters (God of War, Dark Souls, etc.)
2. Small Team Achievers (Hades, Hollow Knight, etc.) ← CRITICAL
3. Episodic Successes (Hitman, Life is Strange, etc.)
4. Cultural Authenticity (Ghost of Tsushima, etc.)
5. Mythology Adaptations (Hades, God of War, etc.)
6. Budget Champions (Undertale, Celeste, etc.) ← CRITICAL
7. Stylized Art Wins (Okami, Hades, etc.)
8. Hardware Friendly (runs on low-end PCs)
9. Persian Adjacent (Prince of Persia, AC: Mirage, etc.)
10. Wildcard Inspirations (unexpected lessons)

**Process:**
```
1. Copy: docs/benchmarks/_template/FIND_GAMES_PROMPT.md
2. Paste into Claude Deep Research (no customization needed!)
3. Wait 30-60 minutes
4. Receive comprehensive game list
5. Save to: docs/benchmarks/MASTER_GAME_LIST.md
6. Create folders for Tier 1 games
7. Proceed to Step 1 for individual analysis
```

**Expected output:**
- Tier 1 (HIGH): 10-15 games to analyze immediately
- Tier 2 (MEDIUM): 10-15 games for month 2
- Tier 3 (LOW): 10-15 games as needed
- Analysis roadmap (week-by-week plan)

**Do this ONCE at project start!**

---

### Step 1: Analyze Individual Games ⭐⭐

Use the comprehensive research prompt at `_template/CLAUDE_DEEP_RESEARCH_PROMPT.md`:

**Advantages:**
- ✅ Searches web, YouTube, reviews automatically
- ✅ Compiles data from multiple sources
- ✅ Structured output ready to save
- ✅ ~30 minutes vs 1-8 hours manual research
- ✅ Consistent analysis quality
- ✅ Finds sources you might miss

**Process:**
```
1. Open: docs/benchmarks/_template/CLAUDE_DEEP_RESEARCH_PROMPT.md
2. Replace [GAME_NAME] with target (e.g., "Hades")
3. Copy entire prompt
4. Paste into Claude Deep Research
5. Wait for comprehensive analysis
6. Save to docs/benchmarks/[game-name]/[game-name].md
```

**When to use manual research instead:**
- Game is very obscure (little online info)
- Need hands-on gameplay experience
- Verifying specific technical details

### Using Benchmarks with AI Tools

#### Prompting Claude for Implementation

```
"Based on docs/benchmarks/[game-name]/, suggest how we can implement
[specific feature] for Shahnameh given our constraints:
- 2-person team + Claude Code
- Free/local AI tools only
- Godot/Unreal Engine
- Episodic structure
- Persian cultural authenticity required"
```

### Extracting Design Patterns

```
"Compare combat systems from docs/benchmarks/god-of-war-2018/ and
docs/benchmarks/dark-souls/. Design a combat system for Shahnameh
that combines the best elements while being achievable for our team."
```

### Business Planning

```
"Review episodic strategies from docs/benchmarks/hitman/ and
docs/benchmarks/life-is-strange/. Recommend pricing and release
schedule for Shahnameh's 3-episode plan."
```

---

## Contributing New Benchmarks

### Priority Queue

**Next to Analyze:**
1. Prince of Persia: The Sands of Time (Persian setting)
2. Blasphemous (small team, cultural mythology)
3. A Plague Tale: Innocence (small team AAA quality)
4. Sifu (indie combat excellence)
5. Assassin's Creed: Mirage (recent Middle Eastern game)

### Analysis Process

**Option A: AI-Powered (Recommended) ⭐**

1. **Open:** `docs/benchmarks/_template/CLAUDE_DEEP_RESEARCH_PROMPT.md`
2. **Customize:** Replace `[GAME_NAME]` with target game
3. **Copy prompt** and paste into Claude Deep Research
4. **Let Claude research** (~10-30 minutes)
5. **Review output** and save to `docs/benchmarks/[game-name]/[game-name].md`
6. **Update this README** (change status to ✅ Complete)

**Time:** 30 minutes to 1 hour (mostly automated)

**Option B: Manual Analysis (Traditional)**

1. **Create folder:** `mkdir docs/benchmarks/[game-name]`
2. **Copy template:** `cp docs/benchmarks/_template/GAME_NAME.md docs/benchmarks/[game-name]/`
3. **Research (1-8 hours):**
   - Official sources (dev interviews, GDC talks)
   - Reviews (Metacritic, Steam, YouTube)
   - Community (Reddit, Discord, wikis)
4. **Fill template** (focus on Key Takeaways section)
5. **Update this README** (add to status table)
6. **Reference in CLAUDE.md** (if applicable)

**Time:** 1-8 hours depending on depth

### Quality Standards

**Minimum Viable Benchmark:**
- Quick Reference section complete
- Business Model filled out
- User Reception summary
- Key Takeaways with 3+ actionable insights

**Complete Benchmark:**
- All template sections filled
- Sources cited
- Visual references (screenshots, links)
- Updated quarterly or when new data available

---

## Benchmark-Driven Development

### Phase 1: Pre-Production (Current)
**Use benchmarks for:**
- Scope validation (compare to small team games)
- Feature prioritization (what works, what doesn't)
- Art direction (stylized vs realistic costs)
- Business model refinement

### Phase 2: Production
**Use benchmarks for:**
- Combat feel reference (God of War, Dark Souls)
- Boss design patterns (Dark Souls, Hades)
- Narrative pacing (Hellblade, Ghost of Tsushima)
- Cultural authenticity checks (Ghost of Tsushima)

### Phase 3: Polish & Release
**Use benchmarks for:**
- Marketing strategies (indie success stories)
- Pricing decisions (episodic models)
- Community management (successful launches)
- Post-launch planning (updates, DLC)

---

## Cross-References

**To GDD:** `docs/consultants/5_shahnameh_gdd.md`
- Combat pillar → God of War, Dark Souls benchmarks
- Story pillar → Hellblade, Ghost of Tsushima benchmarks
- Episodic structure → Hitman, Life is Strange benchmarks

**To AI Tools:** `docs/consultants/7_free_ai_tools_guide.md`
- Asset creation → How benchmarked games made assets
- Budget comparison → What they spent vs what we can do free

**To CLAUDE.md:** Main repository guide
- References this folder for competitive analysis
- AI agents should consult benchmarks when designing features

---

## Quick Command Reference

```bash
# Create new benchmark
mkdir docs/benchmarks/[game-name]
cp docs/benchmarks/_template/GAME_NAME.md docs/benchmarks/[game-name]/

# List all benchmarks
ls docs/benchmarks/

# Search all benchmarks for keyword
grep -r "keyword" docs/benchmarks/ --include="*.md"

# Find games with specific feature
grep -r "episodic" docs/benchmarks/ --include="*.md"
```

---

**Last Updated:** 2025-12-26

**Total Benchmarks:** 5 templates ready, 0 complete analyses
**High Priority Remaining:** 5
**Medium Priority Remaining:** 5
**Low Priority Remaining:** 2
