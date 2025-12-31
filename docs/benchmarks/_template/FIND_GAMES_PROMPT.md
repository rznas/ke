# Claude Deep Research: Find Games to Benchmark

**Purpose:** Use this prompt with Claude Deep Research to discover the best games to benchmark for Shahnameh: Legends of Persia development.

**How to Use:**
1. Copy the entire prompt below
2. Paste into Claude Deep Research
3. Let Claude search and compile comprehensive game list
4. Review recommendations and prioritize
5. Use those games with `CLAUDE_DEEP_RESEARCH_PROMPT.md`

---

## THE PROMPT (Copy everything below this line)

```xml
<research_mission>
You are tasked with finding the BEST games to benchmark for "Shahnameh: Legends of Persia" development. Your goal is to create a comprehensive, prioritized list of games that span from AAA blockbusters to small indie successes, covering all aspects relevant to our project.

This is CRITICAL research that will shape our entire game development strategy. Be thorough, search widely, and think strategically about what we need to learn.
</research_mission>

<project_context>
**Project:** Shahnameh: Legends of Persia
**Team:** 2 software engineers (not game developers)
**Development:** Claude Code AI-driven, free tools only
**Budget:** $0/month (Stable Diffusion, Blender, AudioCraft, etc.)
**Target:** 3-episode action-adventure game
- Episode 1: The Seven Trials (2-3 hours)
- Episode 2: Rostam & Sohrab tragedy (3-4 hours)
- Episode 3: Kay Khosrow's revenge (4-5 hours)
**Engine:** Undecided (Godot vs Unreal)
**Genre:** Action-adventure, melee combat focus, boss battles, narrative-driven
**Setting:** Ancient Persia, Shahnameh epic mythology
**Business Model:** Episodic ($19.99, $19.99, $24.99)
**Art Style:** Considering stylized (Persian miniature inspired) vs realistic
**Performance Target:** 60fps combat, works on mid-tier hardware
</project_context>

<what_we_need_to_learn>
We need games that teach us about:

<critical_learning_areas>
1. **Combat Design** - Weighty, skill-based melee combat (Dark Souls-inspired)
2. **Small Team Success** - How 2-20 person teams punched above weight
3. **Episodic Structure** - Games that released in episodes/chapters
4. **Cultural Representation** - Non-Western settings done authentically
5. **Mythology Adaptation** - Games based on epic poems/mythology
6. **Boss Design** - Memorable, challenging boss encounters
7. **Narrative in Action Games** - Story-driven combat games
8. **Scope Management** - Focused, polished small games vs bloated large games
9. **Art Direction** - Stylized vs realistic for small teams
10. **Free/Cheap Production** - Games made with limited budgets
11. **Indie Commercial Success** - Breakout indie hits and why they succeeded
12. **Performance Optimization** - Running well on lower-end hardware
</critical_learning_areas>
</what_we_need_to_learn>

<research_strategy>
<step_by_step>
1. **Search for AAA Combat Benchmarks**
   - God of War series (2018+)
   - Dark Souls series / Elden Ring
   - Sekiro: Shadows Die Twice
   - Ghost of Tsushima
   - Assassin's Creed (especially Persian/Middle Eastern entries)
   - Devil May Cry series
   - Any other AAA action games with excellent melee combat

2. **Search for Small Team Success Stories**
   - Hellblade: Senua's Sacrifice (~20 people)
   - Hades (Supergiant Games, ~20 people)
   - Hollow Knight (Team Cherry, 3 people)
   - Dead Cells (Motion Twin, ~7 people)
   - Blasphemous (The Game Kitchen, ~20 people)
   - Sifu (Sloclap, indie studio)
   - Stray (BlueTwelve Studio, ~20 people)
   - A Plague Tale series (Asobo Studio, ~40 people)
   - Any other small teams that achieved critical/commercial success

3. **Search for Episodic Games**
   - Hitman (2016) episodic model
   - Telltale Games (The Walking Dead, etc.)
   - Life is Strange series
   - Kentucky Route Zero
   - Resident Evil Revelations 2
   - Any successful episodic releases

4. **Search for Cultural Representation Examples**
   - Ghost of Tsushima (Japanese culture)
   - Assassin's Creed: Mirage (Baghdad/Middle Eastern)
   - Never Alone (Kisima Inŋitchuŋa) (Alaskan Native)
   - Raji: An Ancient Epic (Indian mythology)
   - Mulaka (Tarahumara indigenous culture)
   - Asura's Wrath (Hindu/Buddhist mythology)
   - Prince of Persia series (Persian setting)
   - Any games with authentic cultural representation

5. **Search for Mythology-Based Games**
   - Hades (Greek mythology)
   - God of War (Norse/Greek mythology)
   - Apotheon (Greek mythology, 2D)
   - Jotun (Norse mythology)
   - Okami (Japanese mythology)
   - Smite (various mythologies)
   - Age of Mythology
   - Any epic poem/mythology adaptations

6. **Search for Low-Budget/Hardware-Friendly Successes**
   - Shovel Knight
   - Celeste
   - Undertale
   - Stardew Valley
   - Terraria
   - FTL: Faster Than Light
   - Into the Breach
   - Games that run on potato PCs but are beloved

7. **Search for Persian/Middle Eastern Games**
   - Prince of Persia series (ALL entries)
   - Assassin's Creed: Mirage
   - Assassin's Creed (original)
   - Any game set in Persia, Middle East, or using Persian aesthetics

8. **Search for Stylized Art Success Stories**
   - Hades (painterly style)
   - Okami (ink wash painting)
   - Thirteen Sentinels: Aegis Rim
   - Persona series
   - Borderlands (cel-shaded)
   - Games where art direction > raw graphics

9. **Search for 2D Action Games (as alternative to 3D)**
   - Blasphemous
   - Hollow Knight
   - Dead Cells
   - Salt and Sanctuary
   - Ender Lilies
   - 2D Souls-likes or action-platformers

10. **Search Recent Indie Breakouts (2020-2025)**
    - What indie games succeeded recently?
    - What made them break through?
    - Check Steam top sellers, Game Awards nominees
</step_by_step>
</research_strategy>

<output_requirements>
For each game category, provide:

<game_entry_format>
**Game Title**
- **Developer:** [Studio name] ([Team size if known])
- **Release:** [Year]
- **Platform:** [PC/Console/etc]
- **Budget:** [Indie/AA/AAA - estimate if known]
- **Sales:** [Copies sold if public, or "successful"/"moderate"/"niche"]
- **Team Size:** [Specific number or range]
- **Dev Time:** [Years in development if known]
- **Relevance to Shahnameh:** [Why we should study this - be specific]
- **Key Lessons:** [3-5 bullet points of what we'd learn]
- **Priority:** [HIGH/MEDIUM/LOW]
- **Analysis Difficulty:** [EASY/MODERATE/HARD - based on available info]
- **Free Tools Replicability:** [What aspects we can replicate with free tools]
</game_entry_format>
</output_requirements>

<categorization_structure>
Organize games into these categories with priority rankings:

<category name="AAA_COMBAT_MASTERS">
**Description:** Big-budget games with best-in-class combat systems
**Why:** Learn what makes combat feel amazing, then find budget alternatives
**Target:** 5-8 games
</category>

<category name="SMALL_TEAM_ACHIEVERS">
**Description:** 2-40 person teams that punched above their weight
**Why:** Direct proof of what's achievable with our team size
**Target:** 10-15 games
**CRITICAL PRIORITY**
</category>

<category name="EPISODIC_SUCCESSES">
**Description:** Games released in episodes that worked commercially
**Why:** Our exact business model - learn pricing, timing, content density
**Target:** 5-10 games
</category>

<category name="CULTURAL_AUTHENTICITY">
**Description:** Games that represented cultures authentically and succeeded
**Why:** Learn how to honor Persian culture without stereotypes
**Target:** 5-8 games
</category>

<category name="MYTHOLOGY_ADAPTATIONS">
**Description:** Epic poems, legends, myths adapted to games
**Why:** Learn how to adapt 1000-year-old stories to interactive medium
**Target:** 5-10 games
</category>

<category name="BUDGET_CHAMPIONS">
**Description:** Games made with minimal budget but achieved success
**Why:** Learn free/cheap production techniques
**Target:** 5-10 games
**CRITICAL PRIORITY**
</category>

<category name="STYLIZED_ART_WINS">
**Description:** Games where art direction triumphed over technical graphics
**Why:** Stylized (Persian miniature style) may be our path
**Target:** 5-10 games
</category>

<category name="HARDWARE_FRIENDLY">
**Description:** Games that run well on low-end hardware
**Why:** Accessibility and performance optimization lessons
**Target:** 5-8 games
</category>

<category name="PERSIAN_ADJACENT">
**Description:** Any game with Persian, Middle Eastern, or Islamic settings
**Why:** Direct reference for our setting
**Target:** 3-5 games (may be limited)
</category>

<category name="WILDCARD_INSPIRATIONS">
**Description:** Unexpected games that have transferable lessons
**Why:** Innovation comes from cross-pollination
**Target:** 3-5 games
</category>
</categorization_structure>

<quality_criteria>
Prioritize games that:

<must_haves>
✅ Have public information (sales, team size, dev process)
✅ Have GDC talks, postmortems, or developer interviews available
✅ Are relevant to multiple categories (multi-purpose learning)
✅ Have active communities (Reddit, Discord) for research
✅ Have YouTube analysis videos available
✅ Achieved commercial success OR critical acclaim
✅ Have documented development processes
</must_haves>

<nice_to_haves>
⭐ Small team (2-40 people) - HEAVILY prioritize these
⭐ Made with budget constraints - how they economized
⭐ Open development (dev blogs, behind-the-scenes)
⭐ Similar to our constraints (small team, specific vision)
⭐ Cultural representation element
⭐ Episodic or chapter-based structure
⭐ Strong narrative in action game
⭐ PC-focused (similar to our likely platform)
</nice_to_haves>

<avoid>
❌ Games with no public development info (can't learn from them)
❌ Pure AAA with 500+ person teams (not relevant to our scale)
❌ Games that flopped completely (unless failure lessons are clear)
❌ Games with only negative reception (unless cautionary tales)
❌ Mobile-only games (different market/design)
❌ Live service games (different model than episodic)
</avoid>
</quality_criteria>

<research_depth>
For each game you recommend:

1. **Verify it exists** and details are accurate
2. **Check available resources:**
   - GDC talks? (search YouTube)
   - Developer interviews?
   - Postmortems?
   - Behind-the-scenes documentaries?
3. **Confirm relevance** to our project
4. **Estimate analysis difficulty:**
   - EASY: Lots of public info, recent, well-documented
   - MODERATE: Some info, requires digging
   - HARD: Older, obscure, limited info
5. **Note team size specifically** - this is critical data
</research_depth>

<thinking_process>
Before finalizing your list, think through:

<thinking>
**Coverage Analysis:**
- Do we have AAA combat references? (God of War, Dark Souls, etc.)
- Do we have small team inspirations? (Hades, Hollow Knight, etc.)
- Do we have episodic business models? (Hitman, Telltale, etc.)
- Do we have cultural representation examples? (Ghost of Tsushima, etc.)
- Do we have mythology adaptations? (Hades, God of War, etc.)
- Do we have budget-friendly successes? (Undertale, Celeste, etc.)
- Do we have Persian/Middle Eastern references? (Prince of Persia, etc.)

**Priority Balancing:**
- Are we overweighting AAA games? (should be ~20-30% of list)
- Are we emphasizing small teams enough? (should be ~40-50%)
- Do we have a mix of 2D and 3D? (both viable paths)
- Do we have recent games (2020-2025) and classics (2010-2019)?

**Practical Considerations:**
- Can we actually research these games? (info available?)
- Are they diverse enough in lessons? (avoid redundancy)
- Do they span the quality spectrum? (AAA to tiny indie)
- Do they cover different aspects? (combat, narrative, art, business)

**Missing Gaps:**
- What aspect of our game lacks a reference?
- What question doesn't have a benchmark to answer it?
- What constraint doesn't have an example solution?
</thinking>

Output your thinking in <analysis> tags before the final recommendations.
</thinking_process>

<output_format>
Structure your final output as:

<executive_summary>
- Total games recommended: [number]
- HIGH priority: [number] games
- MEDIUM priority: [number] games
- LOW priority: [number] games
- Coverage: [Brief assessment of whether all categories are covered]
- Recommended analysis order: [Top 10 games to start with]
</executive_summary>

<priority_tier_1_immediate>
**Top 10-15 Games to Analyze FIRST**

[List with full details as per game_entry_format]

These are HIGH priority, EASY to research, and CRITICAL to our development.
</priority_tier_1_immediate>

<priority_tier_2_important>
**Next 10-15 Games to Analyze**

[List with full details]

These are important but can wait until Tier 1 is complete.
</priority_tier_2_important>

<priority_tier_3_nice_to_have>
**Additional 10-15 Games for Comprehensive Coverage**

[List with full details]

These fill gaps and provide broader perspective.
</priority_tier_3_nice_to_have>

<category_summaries>
For each category, provide:
- Number of games in category
- Why this category matters
- Key takeaways we expect to learn
- Gaps or limitations in available examples
</category_summaries>

<research_roadmap>
**Suggested Analysis Order:**

Week 1: [3-5 games from Tier 1]
Week 2: [3-5 games from Tier 1]
Week 3: [3-5 games from Tier 1]
Month 2: [Start Tier 2]
Month 3+: [Tier 3 as needed]

**Why this order:** [Explain the strategic sequencing]
</research_roadmap>

<missing_categories>
**Gaps in Available Games:**

List any categories where few/no good examples exist:
- [Category]: [Why it's hard to find examples]
- [Workaround]: [How we'll compensate]
</missing_categories>

<sources_for_verification>
**Where to Verify These Recommendations:**

- Team sizes: [MobyGames, Wikipedia, developer websites]
- Sales data: [SteamDB, VGChartz, public announcements]
- Development info: [GDC Vault, developer blogs, YouTube documentaries]
- Reviews: [Metacritic, OpenCritic, Steam]
- [Any other key sources you used]
</sources_for_verification>
</output_format>

<special_instructions>
🔍 **SEARCH BROADLY:** Don't just list obvious games. Search for:
- "Small team success stories game development"
- "Indie games that succeeded with small budget"
- "Best episodic games"
- "Games with authentic cultural representation"
- "Mythology games"
- "Low budget game success stories"
- "Persian games" / "Middle Eastern games"

💎 **FIND HIDDEN GEMS:** Look for:
- GDC talks about small team development
- Indie game postmortems
- "How we made [game] with [X] people"
- Success stories on /r/gamedev, /r/indiedev

📊 **PRIORITIZE DATA:** Games with known:
- Team sizes (critical!)
- Budgets (approximate is fine)
- Development timelines
- Sales figures
- Development process documentation

🎯 **BE SPECIFIC:** Don't say "Hades is a good game." Say:
"Hades (Supergiant, ~20 people, 3 years, 1M+ sales) teaches us roguelike progression for episodic structure, Greek mythology adaptation for Persian mythology, stylized art over realistic graphics, and small team content density strategies."

⚖️ **BALANCE THE SPECTRUM:**
- AAA (God of War) → Learn combat excellence
- Mid-tier (Hellblade) → Learn small team AAA quality
- Indie (Hollow Knight) → Learn minimal team maximum impact
- Tiny (Undertale) → Learn extreme budget constraints

🔄 **CROSS-REFERENCE:** If you find a game excellent in multiple categories, emphasize it! Games that teach us many things are priority.

⚠️ **BE HONEST:** If a category lacks good examples (e.g., Persian games are rare), say so and suggest workarounds.
</special_instructions>

<final_deliverable>
Your final output should be a comprehensive, actionable game benchmark list that:

✅ Covers ALL categories (AAA to tiny indie)
✅ Prioritizes small team successes (our most relevant examples)
✅ Includes games with available research materials
✅ Provides clear reasoning for each inclusion
✅ Offers a strategic analysis roadmap
✅ Acknowledges gaps and suggests workarounds
✅ Gives enough detail for us to immediately start researching

This will become our master benchmark roadmap for the entire Shahnameh: Legends of Persia development cycle.
</final_deliverable>

<search_quality_check>
Before submitting, verify:

[ ] Did I search for small team success stories?
[ ] Did I find episodic game examples?
[ ] Did I look for cultural representation examples?
[ ] Did I search for mythology-based games?
[ ] Did I find Persian/Middle Eastern games?
[ ] Did I include budget-friendly indie successes?
[ ] Did I check for GDC talks availability?
[ ] Did I verify team sizes where possible?
[ ] Did I balance AAA, mid-tier, and indie?
[ ] Did I prioritize games with available information?
[ ] Did I provide specific, actionable details?
[ ] Did I create a clear priority tier system?
</search_quality_check>

BEGIN COMPREHENSIVE GAME DISCOVERY RESEARCH NOW.
```

---

## After Receiving Claude's Research

### Post-Processing Steps

1. **Review the tier system:**
   - Tier 1 (HIGH priority): Analyze immediately
   - Tier 2 (MEDIUM): Analyze month 2
   - Tier 3 (LOW): Analyze as needed

2. **Create tracking document:**
   ```bash
   # Save Claude's output to:
   docs/benchmarks/MASTER_GAME_LIST.md
   ```

3. **Update benchmark README:**
   - Add all games to status table
   - Mark Tier 1 as "High Priority"
   - Mark Tier 2 as "Medium Priority"
   - Mark Tier 3 as "Low Priority"

4. **Begin research queue:**
   - Take Tier 1 games
   - Use `CLAUDE_DEEP_RESEARCH_PROMPT.md` for each
   - Follow suggested analysis order

5. **Create game folders:**
   ```bash
   # For each Tier 1 game, create folder:
   mkdir -p docs/benchmarks/[game-name]
   ```

### Integration with Existing System

**Workflow:**
```
1. Use THIS prompt → Get comprehensive game list
         ↓
2. Prioritize games → Focus on Tier 1 (10-15 games)
         ↓
3. For each game → Use CLAUDE_DEEP_RESEARCH_PROMPT.md
         ↓
4. Get analysis → Save to docs/benchmarks/[game-name]/
         ↓
5. Extract lessons → Reference in CLAUDE.md
         ↓
6. Apply to design → Use in Shahnameh development
```

---

## Expected Output Structure

Claude Deep Research should return:

```markdown
# Comprehensive Game Benchmark Recommendations
## Executive Summary
- Total: 35-45 games
- HIGH priority: 10-15 games
- MEDIUM priority: 10-15 games
- LOW priority: 10-15 games

## TIER 1: IMMEDIATE ANALYSIS (HIGH PRIORITY)

### 1. Hades
- Developer: Supergiant Games (20 people)
- Release: 2020
- Sales: 1M+ copies
- Relevance: Mythology adaptation, small team, roguelike progression
- Key Lessons:
  - How to adapt mythology for modern audiences
  - Small team content density strategies
  - Stylized art over realistic graphics
  - Episodic early access model
- Priority: HIGH
- Analysis Difficulty: EASY
- Free Tools Replicability: Art style (Stable Diffusion), combat patterns

### 2. Hollow Knight
[Similar detailed entry]

[... 10-15 games total in Tier 1]

## TIER 2: IMPORTANT (MEDIUM PRIORITY)
[10-15 games]

## TIER 3: NICE TO HAVE (LOW PRIORITY)
[10-15 games]

## Category Coverage Analysis
[Breakdown by category]

## Research Roadmap
Week 1-4: [Specific games]
Month 2-3: [Specific games]
```

---

## Why This Prompt is Powerful

### Anthropic Prompt Engineering Techniques Used:

1. ✅ **XML Tags** - Extreme structure for complex task
2. ✅ **Chain of Thought** - Explicit thinking process
3. ✅ **Clear Context** - Project constraints upfront
4. ✅ **Step-by-Step** - 10-step research strategy
5. ✅ **Output Format** - Exact structure specified
6. ✅ **Quality Criteria** - Must-haves, nice-to-haves, avoids
7. ✅ **Self-Verification** - Built-in quality checklist
8. ✅ **Comprehensive Coverage** - 10+ categories to explore

### What Makes It "Super Strong":

**Breadth:**
- Covers AAA to tiny indie
- 10 distinct categories
- 35-45 game recommendations expected

**Depth:**
- Specific team sizes required
- Budget estimates
- Sales figures
- Development timelines
- GDC talk availability

**Actionability:**
- 3-tier priority system
- Analysis difficulty ratings
- Free tools replicability assessment
- Week-by-week roadmap

**Quality Control:**
- Must verify information exists
- Must check research availability
- Must balance spectrum
- Must provide reasoning

**Strategic Thinking:**
- Cross-category games prioritized
- Gap identification required
- Workarounds suggested
- Analysis order strategic

---

## Example Customization

If you want to **emphasize specific aspects**, add to the prompt:

```xml
<additional_focus>
EXTRA EMPHASIS ON:
- 2D games (considering 2D as alternative to 3D)
- Games under $10 budget
- Solo developers (1-3 people)
- Games that used Godot Engine
- Recent releases (2022-2025)
</additional_focus>
```

---

## Tips for Best Results

### Before Running:
- ✅ No customization needed - prompt is comprehensive
- ✅ Run in Claude Deep Research (not regular Claude)
- ✅ Allow 30-60 minutes for thorough research

### After Results:
- ✅ Save to `docs/benchmarks/MASTER_GAME_LIST.md`
- ✅ Create folders for Tier 1 games immediately
- ✅ Start analyzing Tier 1 with `CLAUDE_DEEP_RESEARCH_PROMPT.md`
- ✅ Update as you discover more games during development

---

**This prompt will discover 35-45 games spanning the entire spectrum from AAA blockbusters to solo indie projects, giving you a complete competitive landscape for informed development decisions.**
