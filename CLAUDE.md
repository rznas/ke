# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Shahnameh: Legends of Persia** - A game development project adapting the epic Persian poem Shahnameh into an interactive experience. This is a pre-production phase project where the team is exploring game design, choosing between game engines (Godot vs Unreal Engine), and planning implementation with heavy AI assistance.

**Team Size:** 2 developers (software engineers, not game developers by background)
**Development Approach:** AI-agent driven development with Claude Code (claude.ai/code)
**Coding Tool:** Claude Code CLI - all development done through AI agent
**Current Phase:** Pre-production, design exploration, engine selection
**Target:** Episodic action-adventure game focused on Persian mythology
**Budget:** Minimal - prefer free, open-source, and local AI tools (on-demand only)

---

## Repository Structure

```
kingsepic/
├── docs/                           # All documentation and planning
│   ├── consultants/                # Chat flow with Claude documenting design decisions
│   │   ├── 1_first_step.md        # Initial roadmap and AI tools overview
│   │   ├── 2_characters_timeline.md
│   │   ├── 3_starting.md          # Scope recommendations
│   │   ├── 4_*.md                 # Various design documents (dependencies, flow, priorities)
│   │   ├── 5_shahnameh_gdd.md     # Complete Game Design Document (PRIMARY REFERENCE)
│   │   ├── 6_ai_tools_comprehensive.md  # Complete AI tools guide (REPLACED by 7_*)
│   │   └── 7_free_ai_tools_guide.md  # Free/Local AI tools guide (CURRENT)
│   ├── benchmarks/                # Competitive analysis of similar games
│   │   ├── _template/             # Templates for game analysis
│   │   │   ├── GAME_NAME.md       # Complete game benchmark template
│   │   │   ├── VIDEO_ANALYSIS_TEMPLATE.md  # YouTube video analysis template
│   │   │   ├── YOUTUBE_ANALYSIS_GUIDE.md   # Guide for analyzing videos
│   │   │   └── README.md          # How to use templates
│   │   ├── README.md              # Overview of all benchmarks
│   │   ├── hades/                 # Hades game analysis (template ready)
│   │   ├── god-of-war-2018/       # God of War analysis (template ready)
│   │   ├── ghost-of-tsushima/     # Ghost of Tsushima analysis (template ready)
│   │   ├── dark-souls/            # Dark Souls analysis (template ready)
│   │   └── hellblade/             # Hellblade analysis (template ready)
│   ├── engine/
│   │   ├── godot/                 # Godot Engine documentation (LLM-optimized)
│   │   │   ├── classes/           # 1,066 JSON files with complete API reference
│   │   │   └── README.md          # How to use Godot docs with LLMs
│   │   └── unreal_engine/         # (placeholder for Unreal docs)
│   └── knowledge/
│       └── prompt_engineering/    # Anthropic's prompt engineering best practices
├── src/                           # Source code (currently exploratory)
│   ├── godot/                     # Godot prototypes/experiments
│   └── unreal_engine/             # Unreal prototypes/experiments
└── .claude/                       # Claude Code configuration
```

---

## Critical Documents

### Primary References (READ THESE FIRST)

1. **`docs/consultants/5_shahnameh_gdd.md`** - Complete Game Design Document
   - Full 3-episode game design
   - Episode 1: The Seven Trials (2-3 hours)
   - Episode 2: The Tragedy of Sohrab (3-4 hours)
   - Episode 3: Blood of Kings (4-5 hours)
   - Contains: mechanics, story structure, character designs, technical specs

2. **`docs/consultants/7_free_ai_tools_guide.md`** - Free AI Tools Pipeline (CURRENT)
   - Complete free/local AI toolkit ($0/month)
   - Stable Diffusion, Blender, AudioCraft, etc.
   - Integration workflows for assets
   - Replaces older `6_ai_tools_comprehensive.md` (which had paid tools)

3. **`docs/benchmarks/README.md`** - Competitive Analysis System
   - Templates for analyzing similar games
   - YouTube video analysis capabilities
   - Benchmark status and priorities
   - Integration with design decisions

4. **`docs/consultants/4_recommended_game_flow.md`** - Episodic Structure
   - Mermaid diagram of complete game flow
   - Development timeline integration
   - Asset reuse strategy

### Supporting Documents

- **`docs/consultants/1_first_step.md`** - Initial roadmap, Unreal Engine focus
- **`docs/consultants/3_starting.md`** - Scope recommendations for 2-person team
- **`docs/consultants/4_game_dev_priority.md`** - Development path decision matrix
- **`docs/consultants/2_characters_timeline.md`** - Character dependency tracking
- **`docs/consultants/4_story_arcs_and_dependencies.md`** - Story structure

---

## Game Benchmarking System

### Purpose

The `docs/benchmarks/` directory contains competitive analysis of games similar to Shahnameh. This helps inform design decisions with real-world examples.

### How to Use Benchmarks

**When designing features, reference relevant benchmarks:**

```
Implementing combat? Check:
- docs/benchmarks/god-of-war-2018/
- docs/benchmarks/dark-souls/
- docs/benchmarks/hades/

Planning episodic release? Check:
- Hitman (2016) episodic model analysis
- Life is Strange episodic structure

Ensuring cultural authenticity? Check:
- docs/benchmarks/ghost-of-tsushima/ (Japanese culture handling)
```

### AI-Powered Research Capability ⭐⭐⭐

**Two-phase AI research system:**

#### Phase 1: Discover Games (Do This First!)

Use `_template/FIND_GAMES_PROMPT.md` to discover 35-45 games to benchmark:

**What it does:**
- Searches entire game industry (AAA to tiny indie)
- Finds small team success stories (most relevant to us)
- Creates 3-tier priority system (immediate/important/nice-to-have)
- Provides strategic week-by-week analysis roadmap
- Covers 10 categories: combat, episodic, mythology, cultural, budget, etc.

**Output:** Master game list saved to `MASTER_GAME_LIST.md`

**Time:** Run once at project start (~30-60 minutes)

#### Phase 2: Analyze Individual Games

Use `_template/CLAUDE_DEEP_RESEARCH_PROMPT.md` for each game:

**What it does:**
- Searches web, YouTube, reviews, forums automatically
- Analyzes business models, mechanics, team size, scope
- Extracts lessons specific to 2-person team with free tools
- Outputs structured analysis ready to save
- Includes source URLs for verification

**How to use:**
1. Get game name from MASTER_GAME_LIST.md (Tier 1)
2. Open `docs/benchmarks/_template/CLAUDE_DEEP_RESEARCH_PROMPT.md`
3. Replace `[GAME_NAME]` with target game
4. Copy prompt into Claude Deep Research
5. Receive comprehensive benchmark in ~30 minutes
6. Save to `docs/benchmarks/[game-name]/[game-name].md`

**Manual video analysis also available:**
- **`_template/VIDEO_ANALYSIS_TEMPLATE.md`** - Template for analyzing videos
- **`_template/YOUTUBE_ANALYSIS_GUIDE.md`** - Complete guide for video analysis
- Use when you want detailed timestamp-by-timestamp analysis

### Benchmark Priorities

**High Priority (Start Here):**
- Hades - Indie success, mythology, combat
- God of War - AAA combat, mythology
- Ghost of Tsushima - Cultural representation
- Dark Souls - Boss design, difficulty
- Hellblade - Small team AAA quality

**See `docs/benchmarks/README.md` for complete list and status**

---

## Engine Decision Status

### Current State: UNDECIDED

The team is evaluating both engines:

**Godot Engine:**
- Pros: Open source, easier learning curve, better for 2D
- Docs: LLM-optimized documentation in `docs/engine/godot/`
- Classes: 1,066 JSON files with complete API reference
- Status: Has comprehensive LLM-ready documentation

**Unreal Engine 5:**
- Pros: AAA quality, better 3D, MetaHuman integration
- Recommended in: `docs/consultants/1_first_step.md`
- Status: No documentation yet in repo

### When Working on Engine-Specific Code

**DO:**
- Check which engine directory you're working in (`src/godot/` vs `src/unreal_engine/`)
- Reference appropriate documentation
- For Godot: Use the LLM-optimized docs as described in `docs/engine/godot/README.md`
- Maintain neutrality - don't bias toward either engine unless user specifies

**DON'T:**
- Mix engine-specific code/patterns
- Assume an engine has been chosen
- Create cross-engine dependencies

---

## AI-Agent Development Workflow

### Core Principle: Claude Code-Driven Development

**ALL CODING IS DONE THROUGH CLAUDE CODE** - This is not a traditional development workflow.

- **Primary Tool:** Claude Code CLI (claude.ai/code)
- **Code Generation:** Claude writes all code through agent interactions
- **No Traditional IDE:** Development happens through conversational AI sessions
- **AI Tools:** Prefer free, open-source, locally-runnable tools
- **Budget Constraint:** Use on-demand paid tools only when absolutely necessary

This project is designed for **heavy AI agent involvement** in all phases:

### 1. Design Phase (Current)
- Use Claude to explore game design options
- Generate design documents
- Create planning diagrams (Mermaid)
- Evaluate technical feasibility

### 2. Asset Creation Pipeline

**Characters:**
```
Concept (Midjourney)
  → 3D Model (Meshy.ai)
  → Cleanup (Blender)
  → Rigging (Mixamo)
  → Animation (Cascadeur/Mixamo)
  → Faces (MetaHuman for Unreal)
```

**Environments:**
```
Concept (Midjourney/Stable Diffusion)
  → Blockout (Engine primitives)
  → Assets (Quixel Megascans + Meshy.ai)
  → Textures (Substance + AI)
  → Lighting (Engine-specific)
```

**Audio:**
```
Music: AIVA/Suno → arrangement
Voice: Professional actors → ElevenLabs cloning for NPCs
SFX: Audiocraft/libraries
```

### 3. Code Development (via Claude Code)

**ALL CODE IS WRITTEN BY CLAUDE CODE:**
- You (Claude) are the primary developer
- User directs development through natural language
- No manual coding by team members
- Code generation happens in Claude Code sessions

**When Writing Code:**
- For Godot: Reference `docs/engine/godot/classes/class_*.fjson` files
- For Unreal: Research and explain patterns as you implement
- Structure prompts with XML tags for clarity (see `docs/knowledge/prompt_engineering/`)
- Follow Anthropic's prompt engineering best practices
- Write complete, functional code - don't create stubs or placeholders
- Explain your architectural decisions as you code

**Code Organization:**
- Keep engine-specific code in respective directories
- Document AI tool integrations clearly
- Comment complex game logic thoroughly
- Use meaningful commit messages (this may become a git repo)
- Code should be production-ready, not prototype quality

### 4. Documentation

**Always update docs when:**
- Making significant design decisions
- Changing scope or direction
- Discovering new tools or workflows
- Completing major milestones

**Documentation style:**
- Follow existing pattern in `docs/consultants/`
- Use Mermaid diagrams for visual planning
- Include decision rationale
- Reference source materials (Shahnameh verses, game inspirations)

---

## Game Design Reference

### Story Scope (from GDD)

**Recommended Approach:** 3-episode structure
- Episode 1: Rostam's Seven Trials (linear, boss-focused)
- Episode 2: Rostam & Sohrab (dual protagonist, tragedy)
- Episode 3: Kay Khosrow's Revenge (multi-character, political)

**Timeline:** 18-20 months total development
- Months 1-8: Episode 1
- Months 9-14: Episode 2
- Months 15-20: Episode 3

### Core Gameplay Pillars

1. **Epic Combat** - Weighty, Dark Souls-inspired melee
2. **Emotional Storytelling** - Character-driven narrative
3. **Persian Authenticity** - Cultural accuracy and respect
4. **Accessible Depth** - Easy to learn, hard to master

### Technical Targets

**Minimum Specs:**
- 1080p @ 30fps on GTX 1060 equivalent
- 50GB storage
- Focus on 60fps for combat responsiveness

**Performance Priorities:**
1. Combat responsiveness (input <50ms)
2. Stable framerate in battles
3. Smooth camera
4. Minimal pop-in

---

## Working with Godot Documentation

The repository includes LLM-optimized Godot documentation. When working with Godot:

### Quick Access Pattern

```python
# Class reference location
docs/engine/godot/classes/class_{classname}.fjson

# Tutorial location
docs/engine/godot/tutorials/{topic}/{subtopic}.txt
```

### Key Classes (from Godot docs)

**Core:**
- `class_node.fjson` - Base for all scene objects
- `class_characterbody2d.fjson` / `class_characterbody3d.fjson` - Player movement
- `class_animationplayer.fjson` - Animation system

**Combat:**
- `class_rigidbody2d.fjson` / `class_rigidbody3d.fjson` - Physics objects
- `class_area2d.fjson` / `class_area3d.fjson` - Hitboxes, triggers

**UI:**
- `class_control.fjson` - Base UI element

### Using Godot Docs with Claude

Follow the pattern in `docs/engine/godot/README.md`:

```xml
<godot_documentation>
  <class_reference>
    {{Load relevant class JSON}}
  </class_reference>
  <tutorial>
    {{Load relevant tutorial}}
  </tutorial>
</godot_documentation>

<query>
  {{Your question}}
</query>
```

---

## Cultural Context: Shahnameh

### Source Material

**Shahnameh** (Book of Kings) by Ferdowsi (940-1020 CE)
- 50,000+ verses of Persian epic poetry
- 1,000+ years old
- National epic of Iran
- Contains mythology, legend, and history

### Key Characters (for context)

**Rostam** - Greatest Persian hero
- Lives 500+ years
- Son of Zal (raised by Simurgh bird)
- Champion of Iran across 7 generations of kings
- Tragic hero (kills his own son unknowingly)

**Sohrab** - Rostam's son
- Raised in Turan (enemy nation)
- Seeks father but dies by his hand
- Most tragic story in Shahnameh

**Kay Khosrow** - Righteous king
- Grandson of Kay Kavus
- Son of Siavash (murdered by Afrasiyab)
- Brings justice and eventually ascends mysteriously

### Cultural Sensitivity

**IMPORTANT - When generating content:**
- Respect Persian/Iranian cultural heritage
- Consult source material (Shahnameh translations)
- Don't stereotypically portray Middle Eastern cultures
- Iran ≠ "evil", Turan ≠ "evil" (both have noble and corrupt characters)
- Include cultural consultants in planning (noted in GDD)
- Authentic Persian art/architecture references
- Consider Persian poetry/music traditions

---

## AI Tools Integration

### BUDGET CONSTRAINT: FREE & LOCAL TOOLS PRIORITY

The team prefers **free, open-source, and locally-runnable AI tools**. Use paid/cloud tools **only on-demand** when absolutely necessary.

### Primary Free/Local Stack (PRIORITIZE THESE)

1. **Stable Diffusion (local)** - Character and environment concepts
   - Run locally via AUTOMATIC1111 or ComfyUI
   - Models: Free (Hugging Face, Civitai)
   - Cost: $0 (requires GPU)
   - Use: All concept art and 2D assets

2. **Blender** - 3D modeling and animation
   - Open source, completely free
   - Geometry Nodes for procedural content
   - Grease Pencil for 2D in 3D
   - Use: All 3D modeling, rigging, animation

3. **Mixamo** - Character rigging and animation
   - Free (Adobe service)
   - Auto-rigging for humanoid characters
   - Large animation library
   - Use: Base character animations

4. **Quixel Megascans** - Textures and 3D assets
   - Free with Unreal Engine
   - High-quality photogrammetry assets
   - Use: Environment assets (if using Unreal)

5. **Godot Engine** - If chosen as engine
   - Completely free and open source
   - Built-in asset library
   - Use: Entire game development

6. **AudioCraft (Meta)** - Sound and music generation
   - Open source, run locally
   - Text-to-audio capabilities
   - GitHub: facebook/audiocraft
   - Use: SFX and music generation

7. **Bark (Suno)** - Voice generation
   - Open source, run locally
   - Text-to-speech with emotion
   - GitHub: suno-ai/bark
   - Use: Character voices (basic)

8. **XTTS (Coqui)** - Voice cloning
   - Open source, run locally
   - Voice cloning capabilities
   - Use: Voice variety from single recording

9. **Krita** - 2D art and textures
   - Free, open source
   - Good for texture painting
   - AI plugins available
   - Use: 2D art assets, texture touchups

10. **ArmorPaint** - PBR texture painting
    - One-time purchase ($19) or free (GitHub source)
    - Real-time PBR painting
    - Use: Texturing 3D models

### On-Demand Paid Tools (Use Sparingly)

**Only use when free alternatives are insufficient:**

1. **Meshy.ai Free Tier** → Text to 3D (limited monthly credits)
2. **ElevenLabs Free Tier** → Voice (higher quality, 10k chars/month)
3. **Midjourney** → Concept art (only if SD doesn't achieve quality needed)

### Completely Avoid (Too Expensive)

- ❌ GitHub Copilot (coding done by Claude Code, not needed)
- ❌ Substance 3D ($20/month - use Blender + ArmorPaint instead)
- ❌ AIVA Pro (use AudioCraft locally)
- ❌ Commercial 3D asset marketplaces (use Quixel, free Blender assets)

### Free Tool Integration Workflows

**Stable Diffusion Workflow (Local):**
```bash
# Install AUTOMATIC1111 or ComfyUI locally
# Download Shahnameh-appropriate models (Persian art style, fantasy)
# Generate prompts for image AI:
- Reference Persian miniature painting styles
- Include specific cultural details (architecture, clothing)
- Generate 50+ variations (no cost limit when local)
- Iterate based on cultural authenticity
```

**Blender Pipeline (Free):**
```
Concept (Stable Diffusion)
  → Reference images
  → Model in Blender (manual or geometry nodes)
  → Texture in ArmorPaint or Blender
  → Rig with Rigify or Mixamo
  → Animate in Blender or use Mixamo library
  → Export to game engine
```

**Audio Pipeline (Free/Local):**
```
Music: AudioCraft (local) → Audacity (arrangement/mix)
Voice: Bark or XTTS (local) → Audacity (cleanup)
SFX: Freesound.org + AudioCraft
```

**When Using Voice AI (Local Tools):**
- XTTS can clone voices from short samples
- Bark for varied character voices
- Record team member voices for cloning base
- Use Audacity for cleanup and mixing
- Credit all AI-generated content

**Cost Management:**
- Run AI models locally (requires decent GPU)
- Use free tiers before paid options
- Batch processing to maximize efficiency
- Community assets before custom generation

---

## Prompt Engineering Best Practices

The repository includes Anthropic's prompt engineering guides in `docs/knowledge/prompt_engineering/`.

### Key Principles for This Project

1. **Be Clear and Direct** (`be-clear-and-direct.md`)
   - Specify game engine when relevant
   - Reference specific documents
   - Clear success criteria

2. **Use XML Tags** (`use-xml-tags.md`)
   - Structure game design discussions
   - Organize character/story data
   - Separate code from explanation

3. **Chain of Thought** (`chain-of-thought.md`)
   - Break down game systems step-by-step
   - Show design decision reasoning
   - Explain technical tradeoffs

4. **Long Context Tips** (`long-context-tips.md`)
   - Put reference docs at top of context
   - Use structured formats (XML)
   - Quote relevant sections before answering

---

## Development Commands

### This is NOT a buildable project yet

There are no build commands, test commands, or run commands currently. This is in **pre-production/planning phase**.

### When Project Becomes Active

Document commands here as they're established:

```bash
# Godot (when chosen)
# TBD - will add once project structure is finalized

# Unreal Engine (when chosen)
# TBD - will add once project structure is finalized

# Asset Pipeline
# TBD - scripts for AI asset generation and processing
```

---

## Working as an AI Agent in This Repository

### Your Role

You are **THE PRIMARY DEVELOPER** for a 2-person team of software engineers (not game developers) creating their first game. You write all the code through Claude Code CLI.

**Critical Understanding:**
- You don't assist with coding - **you ARE the coder**
- Team members direct you, you implement
- You make technical decisions and explain them
- You write production-ready code, not examples or tutorials
- Team is learning game development through your implementations

### Key Responsibilities

1. **Primary Code Development** ⭐ MAIN ROLE
   - Write all game code through Claude Code CLI
   - Implement complete systems, not snippets
   - Choose appropriate design patterns
   - Optimize for performance (60fps combat target)
   - Write tests when necessary
   - Debug and fix issues
   - Refactor as needed

2. **Design Guidance**
   - Help refine game mechanics
   - Suggest scope appropriate for team size
   - Reference similar games for inspiration
   - Ground suggestions in documented plans

3. **Technical Architecture**
   - Design system architecture
   - Explain technical decisions
   - Plan for episodic structure
   - Ensure code maintainability
   - Consider asset pipeline integration

4. **Free Tool Integration**
   - Guide usage of local AI tools (Stable Diffusion, Blender, etc.)
   - Generate prompts for Stable Diffusion
   - Structure free asset creation workflows
   - Maintain consistency in art direction
   - Avoid paid tools unless necessary

5. **Documentation**
   - Keep design docs updated
   - Document code architecture
   - Create visual diagrams (Mermaid)
   - Maintain CLAUDE.md (this file)
   - Explain implementations clearly

### Decision-Making Authority

**You CAN (and SHOULD):**
- **Write complete, production code** without asking for permission
- **Choose design patterns** and code architecture
- **Implement features** as described by user
- **Debug and fix issues** autonomously
- **Refactor code** for better quality
- Create documentation
- Recommend free/local tools
- Point out potential issues
- Make technical decisions (algorithms, data structures, etc.)

**You CANNOT (require user decision):**
- Choose the game engine (Godot vs Unreal)
- Change core game scope/pillars from GDD
- Use paid tools without user approval
- Alter story/cultural elements without consultation
- Make decisions that affect budget/timeline significantly
- Skip implementing features (no "TODO" or "implement later")

### Context Awareness

**Before implementing solutions, check:**
1. Which engine (if any) is being targeted
2. Current phase (design vs implementation)
3. Relevant docs in `docs/consultants/` (especially GDD)
4. **Benchmarks in `docs/benchmarks/`** - How have similar games solved this?
5. Cultural sensitivity for Persian content
6. Team size limitations (2 people, YOU are the coder)
7. **Budget constraint: FREE TOOLS ONLY** (local AI, open source)
8. Performance targets (60fps combat, 50GB storage)
9. Episodic structure implications

### Communication Style

- **Be direct** - Team is technical, avoid over-explanation
- **Code immediately** - Don't ask permission to write code, just write it
- **Explain as you build** - Document your architectural decisions
- **Reference sources** - Point to specific docs/GDD sections
- **Show tradeoffs** - Explain pros/cons of approaches when multiple paths exist
- **Scope-aware** - Remind about 2-person team + 1 AI coder (you) limitations
- **Free tools first** - Always suggest free/local alternatives before paid
- **Culturally sensitive** - Respect Persian heritage in all content

---

## Episodic Development Strategy

Per the GDD, this is an **episodic release model**:

### Revenue-Funded Development

- Episode 1 revenue funds Episodes 2-3
- Each episode is standalone but connected
- Season pass available from Episode 1 launch

### Technical Implications

**Asset Reuse:**
- Episode 1 establishes base assets (Rostam model, combat system, Persian architecture)
- Episode 2 reuses + adds Sohrab, Turan aesthetics, duel mechanics
- Episode 3 reuses all + adds battlefield systems, multiple playable characters

**Code Architecture:**
- Design for episodic structure from start
- Shared core systems
- Episode-specific content modules
- Save file compatibility across episodes

---

## Current Project Status

**Phase:** Pre-production / Planning
**Engine:** Not decided (evaluating Godot vs Unreal)
**Team:** 2 software engineers + AI tools
**Next Steps (when ready):**
1. Choose game engine (Godot or Unreal)
2. Create vertical slice (one trial from Episode 1)
3. Establish art style with AI tools
4. Build core combat prototype
5. Set up asset pipeline

---

## Quality Standards

### Code Quality
- Clear variable/function names
- Comments for complex game logic
- No premature optimization
- Performance-conscious (60fps combat target)

### Asset Quality
- AI-generated assets require human cleanup
- Cultural authenticity review
- Consistent art style
- Performance budgets (polygon counts, texture sizes)

### Design Quality
- Each episode must be completable
- Combat must feel responsive
- Story must be emotionally resonant
- Cultural representation must be respectful

---

## Resources and References

### External Documentation
- Godot Docs: `docs/engine/godot/` (LLM-optimized)
- Anthropic Prompt Engineering: `docs/knowledge/prompt_engineering/`

### Game Inspirations (from GDD)
- **Combat:** Dark Souls, God of War
- **Narrative:** Hades, Ghost of Tsushima
- **Style:** Prince of Persia, Assassin's Creed (Persian setting)

### Cultural Resources (from consultants docs)
- Shahnameh translations
- Persian miniature painting references
- Persian architecture (Metropolitan Museum, British Museum)
- Iranian game dev communities

### AI Tool Documentation
- Free tools guide: `docs/consultants/7_free_ai_tools_guide.md`
- Integration workflows included
- $0/month budget toolkit

### Competitive Analysis
- Game benchmarks: `docs/benchmarks/`
- YouTube video analysis templates
- Similar games lessons (combat, narrative, scope, business)

---

## Important Reminders

1. **This is pre-production** - No production code exists yet
2. **Engine undecided** - Don't assume Godot or Unreal
3. **Cultural sensitivity** - Persian heritage must be respected
4. **Scope management** - 2-person team, use AI strategically
5. **Episodic structure** - Each episode must be self-contained
6. **AI-first development** - Embrace AI tools, not traditional AAA pipeline
7. **Document decisions** - Update `docs/consultants/` when making significant choices

---

## Questions to Ask User When Unclear

**Only ask when truly necessary - prefer to implement and explain:**

1. "Which game engine should I target for this implementation?" (Godot or Unreal)
2. "This affects core game design [X] - should I reference the GDD first or is this intentional?"
3. "This requires a paid tool [X] - do you approve the cost, or should I use free alternative [Y]?"
4. "I checked benchmarks for [Game X] and [Game Y] - they solve this differently. Which approach fits Shahnameh better?"
5. "This involves cultural content - have you consulted Persian references?"
6. "This seems outside scope for a 2-person + AI team - should we simplify?"
7. "Should this design decision be documented in `docs/consultants/` or as a benchmark note?"

**Don't ask (just do it):**
- "Should I write the code?" - YES, always
- "What design pattern should I use?" - You decide based on best practices
- "Should I add comments?" - YES, always for complex logic
- "Should I handle edge cases?" - YES, write production quality code

---

**Remember:** You're helping build the first major game based on Persian mythology. Make it respectful, make it playable, make it achievable for a 2-person team with AI assistance.
