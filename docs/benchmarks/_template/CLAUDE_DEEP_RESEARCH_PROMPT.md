# Claude Deep Research Prompt Template

**Purpose:** Use this prompt with Claude's Deep Research feature to comprehensively analyze a game for the Shahnameh: Legends of Persia benchmark collection.

**How to Use:**
1. Replace `[GAME_NAME]` with the actual game title
2. Copy the entire prompt below
3. Paste into Claude Deep Research
4. Let Claude research and compile the analysis
5. Save output to `docs/benchmarks/[game-name]/[game-name].md`

---

## THE PROMPT (Copy everything below this line)

```xml
<research_context>
You are conducting competitive analysis for "Shahnameh: Legends of Persia," an episodic action-adventure game based on Persian mythology, being developed by a 2-person software engineering team using AI-assisted development and free/local tools.

Your task is to deeply research [GAME_NAME] and create a comprehensive benchmark analysis that will inform design decisions for Shahnameh.
</research_context>

<project_constraints>
- Team Size: 2 software engineers (not game developers)
- Development Approach: Claude Code AI-driven development
- Budget: $0/month (free tools only - Stable Diffusion, Blender, AudioCraft, etc.)
- Target: 3-episode game (2-3 hours each)
- Genre: Action-adventure with combat focus
- Cultural Focus: Persian mythology (Shahnameh epic poem)
- Engine: Undecided (Godot vs Unreal Engine)

</project_constraints>

<research_instructions>
Research [GAME_NAME] comprehensively and fill out the benchmark template. Use web searches, YouTube videos, reviews, developer interviews, GDC talks, Reddit discussions, and any other credible sources.

<step_by_step_process>
1. **Basic Information Gathering**
   - Release date, platforms, developer, publisher
   - Team size, development time, budget (if publicly known)
   - Sales figures and commercial success
   - Metacritic/review scores

2. **Business Model Analysis**
   - Pricing strategy
   - DLC/episodic structure
   - Monetization approach
   - Revenue estimates
   - Marketing tactics that worked/failed

3. **User Reception Research**
   - Professional reviews (Metacritic, OpenCritic)
   - User reviews (Steam, Reddit, forums)
   - Common praise vs complaints
   - Long-term community sentiment

4. **Core Mechanics Deep Dive**
   - Combat system (if applicable)
   - Progression mechanics
   - Game feel and responsiveness
   - What makes it fun (or not fun)

5. **Narrative & Story**
   - How story is delivered
   - Character development quality
   - Player agency
   - Cultural representation (if applicable)

6. **Technical & Visual**
   - Art style and direction
   - Performance and optimization
   - Engine used and technical innovations
   - Team size vs production quality achieved

7. **Scope & Content**
   - Hours of content
   - Environment/enemy variety
   - Was scope appropriate for team size?
   - Smart scoping decisions

8. **YouTube Video Analysis**
   Search for and analyze:
   - Main reviews (ACG, SkillUp, etc.)
   - GDC talks or developer postmortems
   - Combat analysis videos
   - "Making of" documentaries
   Include timestamps for key insights

9. **Lessons for Shahnameh**
   - What can a 2-person team with free AI tools realistically adopt?
   - What requires larger budget/team?
   - Specific design patterns to emulate
   - Pitfalls to avoid
</step_by_step_process>

<output_structure>
Structure your analysis using these XML-tagged sections:

<game_overview>
- Title, developer, release date
- Quick facts (team size, budget, platforms)
- One-sentence description
- Why this game is relevant to Shahnameh
</game_overview>

<business_analysis>
- Pricing and monetization
- Sales performance
- Marketing approach
- Revenue model
- Lessons for episodic release
</business_analysis>

<user_reception>
- Review scores (critics and users)
- Most common praise (top 3-5 points)
- Most common criticism (top 3-5 points)
- Long-term community sentiment
</user_reception>

<gameplay_mechanics>
- Combat system (if applicable) - detailed breakdown
- Progression systems
- Exploration and world design
- What makes it engaging
- What doesn't work
</gameplay_mechanics>

<narrative_design>
- Story structure
- Character development
- Delivery methods (cutscenes, gameplay, environmental)
- Player choices and agency
- Cultural representation (if applicable)
</narrative_design>

<technical_production>
- Art direction and style
- Engine and tools used
- Team size achievements
- Asset creation pipeline (if known)
- Performance and optimization
</technical_production>

<scope_analysis>
- Content volume (hours, areas, enemies)
- Development time
- Team size vs output quality
- Smart scoping decisions
- Areas where they over/under-scoped
</scope_analysis>

<youtube_videos>
List 5-10 most valuable videos found:
- Title, channel, URL
- Duration and upload date
- Key timestamps
- Main insights from each video
- Which videos are must-watch for Shahnameh team
</youtube_videos>

<feasibility_for_small_team>
What a 2-person team with free AI tools can replicate:
- Achievable elements (✅)
- Difficult but possible with AI (🤔)
- Out of scope / requires budget (❌)
</feasibility_for_small_team>

<key_takeaways>
<combat_lessons>
- What to adopt
- What to avoid
- Specific mechanics applicable to Shahnameh
</combat_lessons>

<narrative_lessons>
- Storytelling techniques
- Cultural representation best practices (if applicable)
- Pacing strategies
</narrative_lessons>

<scope_lessons>
- How they managed scope
- What we can learn for episodic structure
- Content density vs quality balance
</scope_lessons>

<business_lessons>
- Pricing strategy insights
- Marketing on low budget
- Episodic release learnings (if applicable)
</business_lessons>

<technical_lessons>
- Art style choices for small teams
- Free tool alternatives to their pipeline
- Performance optimization priorities
</technical_lessons>

<actionable_insights>
List 10-15 specific, actionable takeaways, such as:
- "Implement Mechanic X using Pattern Y"
- "Price Episode 1 at $Z based on this game's success"
- "Focus art budget on A instead of B"
- "Use free tool C instead of paid tool D"
</actionable_insights>
</key_takeaways>

<sources>
List all sources used:
- Official websites
- Review sites (URLs)
- YouTube videos (URLs with timestamps)
- Developer interviews (URLs)
- Reddit threads (URLs)
- Sales data sources
- Any other references
</sources>
</output_structure>

<thinking_guidelines>
Before writing each section, think through:

<thinking>
- What information is most relevant to Shahnameh development?
- How does this compare to our constraints (2-person team, free tools)?
- What can we realistically implement vs what's aspirational?
- Are there cultural parallels (e.g., Ghost of Tsushima's Japanese culture → our Persian culture)?
- What would a software engineer with no game dev experience need to know?
</thinking>

Output your thinking in <research_notes> tags as you go, then synthesize into the final structured analysis.
</thinking_guidelines>

<research_priorities>
Focus MOST on:
1. ✅ Team size and how they achieved results
2. ✅ Business model and pricing (especially if episodic)
3. ✅ Combat feel and implementation (if applicable)
4. ✅ Scope decisions and content density
5. ✅ Art direction choices (realistic vs stylized)
6. ✅ Cultural representation (if applicable to the game)
7. ✅ Free/cheap asset creation methods (if known)

Focus LESS on:
- ❌ Generic gameplay descriptions everyone knows
- ❌ Full plot summaries (just structure and delivery)
- ❌ Subjective opinions without backing data
- ❌ Unverifiable rumors or speculation
</research_priorities>

<quality_standards>
- Cite sources for all factual claims (sales, team size, budget)
- Distinguish between confirmed facts and estimates
- Note when information is unavailable ("Unknown" not guesses)
- Include specific examples with timestamps/references
- Be honest about what's achievable for a 2-person team
- Don't inflate or deflate the game - objective analysis only
</quality_standards>

<special_focus_areas>
If [GAME_NAME] has any of these, give EXTRA attention:

**If it's from a small team:**
- How did they punch above their weight?
- What shortcuts or smart decisions did they make?
- Tool pipeline and asset reuse

**If it has episodic structure:**
- Episode pricing and timing
- Content per episode
- How they maintained interest between releases
- Revenue model success/failure

**If it involves mythology or cultural setting:**
- Research and authenticity approach
- Community reception from represented culture
- Balance between accuracy and gameplay

**If it has Souls-like combat:**
- Combat feel, weight, and timing
- Boss design patterns
- Difficulty balancing

**If it's indie that succeeded commercially:**
- Marketing on low budget
- What made it break through
- Pricing strategy
</special_focus_areas>

<game_to_research>
GAME: [GAME_NAME]

Additional context (if any):
[Optional: Add any specific aspects you want researched about this game, like "Focus on their episodic model" or "Analyze their Persian setting representation"]
</game_to_research>

<final_instructions>
1. Conduct deep research using web search, YouTube, reviews, forums
2. Think step-by-step through each section before writing
3. Use the structured XML output format provided
4. Provide specific, actionable insights for a 2-person team with free AI tools
5. Include source URLs for verification
6. Be thorough but concise - focus on what matters for Shahnameh development
7. Call out what's achievable vs aspirational for our constraints

Output the complete analysis ready to be saved as:
docs/benchmarks/[game-name]/[game-name].md
</final_instructions>
```

---

## After Receiving Claude's Research

**Post-Processing Steps:**

1. **Review the output** for completeness
2. **Verify key facts** (team size, sales, budget) if claims seem questionable
3. **Add visual references** if Claude mentioned specific videos/screenshots
4. **Fill any gaps** Claude couldn't research (rare details)
5. **Save to proper location:**
   ```bash
   # Create game folder if needed
   mkdir -p docs/benchmarks/[game-name]

   # Save Claude's output
   # File: docs/benchmarks/[game-name]/[game-name].md
   ```

6. **Update benchmark README:**
   - Change status from "⏳ TODO" to "✅ Complete"
   - Add to relevant categories

7. **Extract video analyses:**
   - If Claude found valuable YouTube videos, create individual video analysis files
   - Use `VIDEO_ANALYSIS_TEMPLATE.md` for detailed video breakdowns

---

## Example Usage

**For researching "Hades":**

Replace in prompt:
```xml
<game_to_research>
GAME: Hades

Additional context:
Focus on their roguelike progression system and how it applies to our episodic structure. Also analyze their Greek mythology representation for lessons on adapting Persian mythology.
</game_to_research>
```

**For researching "Hellblade: Senua's Sacrifice":**

Replace in prompt:
```xml
<game_to_research>
GAME: Hellblade: Senua's Sacrifice

Additional context:
Focus heavily on how a ~20-person team achieved AAA quality. Analyze their audio-focused approach as a cost-saving measure. Research their development documentary for pipeline insights.
</game_to_research>
```

---

## Tips for Best Results

### Use Deep Research for:
- ✅ Games with lots of public information
- ✅ Recent games with active communities
- ✅ Games with GDC talks or postmortems
- ✅ Commercial successes with sales data

### May need manual research for:
- ⚠️ Very old games (pre-2010) with limited online info
- ⚠️ Niche indie games with minimal coverage
- ⚠️ Games that flopped and have little post-release data

### Enhance Claude's Research:
After receiving the analysis, you can:
1. Ask Claude to "expand the combat analysis section with more detail"
2. Request: "Find 5 more YouTube videos specifically about boss design"
3. Follow up: "Compare this game's pricing to 3 similar episodic games"

---

## Integration with Existing Templates

**After Deep Research completes:**

1. Claude's output goes into main benchmark file
2. Use `VIDEO_ANALYSIS_TEMPLATE.md` for individual video deep dives
3. Reference `YOUTUBE_ANALYSIS_GUIDE.md` for watching those videos
4. Update `GAME_NAME.md` template sections Claude might have missed

---

## Prompt Engineering Techniques Used

This prompt employs Anthropic's best practices:

✅ **XML Tags** - Clear structure separation
✅ **Chain of Thought** - Step-by-step research process
✅ **Clear Instructions** - Specific, sequential steps
✅ **Context** - Project constraints upfront
✅ **Output Format** - Structured, parseable response
✅ **Think Before Answer** - Explicit thinking guidelines
✅ **Examples** - Special focus area examples

---

## Troubleshooting

**If Claude's output is too generic:**
- Add more specific focus areas in `<game_to_research>`
- Request follow-up: "Dig deeper into [specific aspect]"

**If sources are missing:**
- Ask: "Provide URLs for all factual claims you made"

**If feasibility analysis is unclear:**
- Follow up: "For each 'achievable' item, explain the free tools we'd use"

**If video analysis is weak:**
- Use this prompt first, then manually watch videos using `YOUTUBE_ANALYSIS_GUIDE.md`

---

**Last Updated:** 2025-12-26
**Compatible with:** Claude Deep Research (Opus, Sonnet models)
