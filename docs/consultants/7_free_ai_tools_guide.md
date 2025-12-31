# Free & Local AI Tools Guide for Shahnameh Game Development

**Created:** 2025-12-26
**Budget:** $0/month (free and local tools only)
**Philosophy:** On-demand paid tools only when absolutely necessary

---

## Complete Free/Local Toolkit

### 1. IMAGE GENERATION (Concept Art)

#### Stable Diffusion - LOCAL INSTALLATION ⭐ PRIMARY

**Installation Options:**

**A. AUTOMATIC1111 WebUI (Easiest)**
```bash
# Clone repository
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui

# Run (auto-installs dependencies)
./webui.sh  # Linux/Mac
# or
webui-user.bat  # Windows

# Access at http://localhost:7860
```

**B. ComfyUI (More Control)**
```bash
# Clone repository
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Install dependencies
pip install -r requirements.txt

# Run
python main.py

# Access at http://localhost:8188
```

**Model Sources (Free):**
- **Hugging Face**: huggingface.co/models (Stable Diffusion models)
- **Civitai**: civitai.com (community models)
- **Recommended Models:**
  - Stable Diffusion XL (base model)
  - DreamShaper (fantasy/game art)
  - RealisticVision (realistic characters)
  - Models fine-tuned on Persian art (search Civitai)

**Usage for Game:**
```
Characters:
  - "Persian warrior, ancient armor, Shahnameh style, concept art"
  - Generate 50+ variations (free when local!)

Environments:
  - "Ancient Persian palace, columned halls, sunset lighting, game art"
  - Tile textures: "seamless Persian carpet pattern, top view"
```

**Hardware Requirements:**
- GPU: NVIDIA 6GB+ VRAM (RTX 2060 or better)
- RAM: 16GB+
- Storage: ~10-50GB for models

---

### 2. 3D MODELING & ANIMATION

#### Blender - FREE & OPEN SOURCE ⭐ PRIMARY

**Installation:**
```bash
# Download from blender.org
# Or via package manager:
sudo apt install blender  # Linux
brew install blender      # Mac
# Windows: Download installer
```

**Key Features for Game Dev:**
- Full 3D modeling suite
- Sculpting tools (for characters)
- Geometry Nodes (procedural content)
- Animation system
- Grease Pencil (2D in 3D)
- Python scripting for automation
- Game engine export (FBX, GLTF)

**Blender Add-ons (Free):**
- **MB-Lab**: Character creation
- **Rigify**: Advanced character rigging
- **Animation Nodes**: Procedural animation
- **Asset Browser**: Built-in asset management

**Usage Pipeline:**
```
1. Model character in Blender (or use base mesh from Mixamo)
2. Sculpt details with sculpting tools
3. UV unwrap for textures
4. Rig with Rigify
5. Animate or use Mixamo animations
6. Export FBX/GLTF to game engine
```

**Learning Resources (Free):**
- Blender Guru YouTube channel
- Grant Abbitt (game asset creation)
- Official Blender documentation

---

#### Mixamo - FREE (Adobe Service) ⭐ ANIMATIONS

**Website:** mixamo.com
**Cost:** FREE (requires Adobe account)

**Features:**
- Auto-rigging for humanoid characters
- 2,000+ free animations
- Motion capture quality
- Direct export to game engines

**Workflow:**
```
1. Upload character model (FBX, OBJ)
2. Auto-rig in seconds
3. Preview animations
4. Download with rig + animation
5. Import to Blender or game engine
```

**Best For:**
- Base combat animations (sword, punch, kick)
- Locomotion (walk, run, jump)
- Idles and transitions
- Quick prototyping

---

### 3. TEXTURING & MATERIALS

#### ArmorPaint - $19 ONE-TIME (or free from source)

**Website:** armorpaint.org
**Cost:** $19 one-time OR compile from source (free)

**Build from Source (Free):**
```bash
git clone https://github.com/armory3d/armorpaint.git
cd armorpaint
# Follow build instructions for your platform
```

**Features:**
- Real-time PBR painting
- Layer-based workflow
- Smart materials
- Mask painting
- Export to game-ready textures

**Alternative: Blender Texture Painting (Free)**
- Built into Blender
- PBR workflow support
- Shader nodes for materials
- Less intuitive but completely free

---

#### Quixel Megascans - FREE with Unreal Engine

**Website:** quixel.com/megascans
**Cost:** FREE if using Unreal Engine

**Content:**
- Photogrammetry assets (rocks, vegetation, architecture)
- High-quality PBR materials
- Thousands of assets
- Regular updates

**Note:** Only free with Unreal. If using Godot, use alternative sources.

---

### 4. AUDIO & MUSIC

#### AudioCraft (Meta) - LOCAL AI AUDIO ⭐ PRIMARY

**GitHub:** github.com/facebookresearch/audiocraft
**Cost:** FREE (open source)

**Installation:**
```bash
# Clone repository
git clone https://github.com/facebookresearch/audiocraft.git
cd audiocraft

# Install
pip install -e .

# Models will auto-download on first use
```

**Features:**
- **MusicGen**: Text-to-music generation
- **AudioGen**: Sound effects generation
- **EnCodec**: Audio compression
- Run entirely locally

**Usage:**
```python
from audiocraft.models import MusicGen

# Generate epic Persian battle music
model = MusicGen.get_pretrained('melody')
descriptions = ['epic Persian battle music, orchestral, drums, traditional instruments']
wav = model.generate(descriptions)

# Save
import torchaudio
torchaudio.save('battle_theme.wav', wav[0].cpu(), model.sample_rate)
```

**For SFX:**
```python
from audiocraft.models import AudioGen

model = AudioGen.get_pretrained('medium')
descriptions = ['sword clash metal', 'footsteps on stone', 'wind desert ambience']
wav = model.generate(descriptions)
```

---

#### Bark (Suno AI) - LOCAL VOICE GENERATION

**GitHub:** github.com/suno-ai/bark
**Cost:** FREE (open source)

**Installation:**
```bash
pip install git+https://github.com/suno-ai/bark.git
```

**Features:**
- Text-to-speech with emotion
- Multiple languages
- Non-verbal sounds (laugh, sigh, etc.)
- Music generation
- Run locally (needs GPU)

**Usage:**
```python
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# Preload models
preload_models()

# Generate speech
text_prompt = "[MAN] The seven trials await you, young Rostam."
audio_array = generate_audio(text_prompt)

# Save
write_wav("rostam_dialogue.wav", SAMPLE_RATE, audio_array)
```

**Speaker Variety:**
- Built-in voice presets
- Can specify speaker: `[v2/en_speaker_6]`

---

#### XTTS (Coqui) - LOCAL VOICE CLONING

**GitHub:** github.com/coqui-ai/TTS
**Cost:** FREE (open source)

**Installation:**
```bash
pip install TTS
```

**Features:**
- Voice cloning from short samples
- Multi-language support
- Real-time synthesis
- Run locally

**Usage:**
```python
from TTS.api import TTS

# Initialize with XTTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Clone voice from sample
tts.tts_to_file(
    text="The Seven Trials await, young warrior.",
    speaker_wav="voice_sample.wav",  # 10-30 seconds of voice
    file_path="output.wav",
    language="en"
)
```

**Workflow:**
- Record team member voices (10-30 seconds each)
- Use as base for different characters
- Adjust pitch/speed in Audacity for variety

---

#### Audacity - FREE AUDIO EDITOR

**Website:** audacityteam.org
**Cost:** FREE (open source)

**Features:**
- Multi-track editing
- Effects and filters
- Noise reduction
- Format conversion
- Plugin support

**Use For:**
- Cleaning AI-generated audio
- Mixing music layers
- Creating sound variations
- Mastering final audio

---

### 5. 2D ART & UI

#### Krita - FREE DIGITAL PAINTING

**Website:** krita.org
**Cost:** FREE (open source)

**Features:**
- Professional digital painting
- Animation tools
- Texture painting
- Layer management
- Brush engine

**Use For:**
- UI mockups
- 2D game assets
- Concept art refinement
- Texture painting

---

#### GIMP - FREE IMAGE EDITING

**Website:** gimp.org
**Cost:** FREE (open source)

**Features:**
- Photoshop alternative
- Layer support
- Advanced editing
- Plugin ecosystem

**Use For:**
- Photo editing
- Texture creation
- UI element creation
- Image manipulation

---

### 6. GAME ENGINE OPTIONS

#### Godot Engine - FREE & OPEN SOURCE ⭐

**Website:** godotengine.org
**Cost:** FREE (MIT license)

**Features:**
- Complete game engine (2D & 3D)
- Visual scripting (Blueprints-like)
- GDScript (Python-like)
- Built-in animation, physics, audio
- Cross-platform export
- No royalties, no fees

**Why Consider:**
- Completely free
- Open source
- Active community
- Good for 2D and lighter 3D
- Easier learning curve
- LLM-optimized docs in this repo

**Cons vs Unreal:**
- Less AAA visual quality
- Smaller asset marketplace
- Less mature 3D features

---

#### Unreal Engine 5 - FREE (5% royalty after $1M)

**Website:** unrealengine.com
**Cost:** FREE (5% royalty after $1M revenue)

**Features:**
- AAA-quality graphics
- Nanite, Lumen
- MetaHuman Creator (free)
- Blueprint visual scripting
- Quixel Megascans (free)
- Large marketplace

**Why Consider:**
- Best visual quality
- MetaHuman for characters
- Free Quixel assets
- Industry standard
- Better for 3D action game

**Cons:**
- Steeper learning curve
- Larger download/storage
- Requires more powerful hardware

---

### 7. VOICE & DIALOGUE

#### Mozilla TTS - FREE VOICE SYNTHESIS

**GitHub:** github.com/mozilla/TTS
**Cost:** FREE (open source)

**Features:**
- Text-to-speech
- Voice cloning
- Multiple languages
- Quality comparable to commercial

---

#### Coqui Studio - FREE TIER

**Website:** coqui.ai
**Cost:** FREE tier available

**Features:**
- Voice cloning
- Emotion control
- Web-based interface
- API access

---

### 8. FREE ASSET LIBRARIES

#### Sounds & Music

**Freesound.org**
- Community sound library
- Creative Commons
- Thousands of SFX
- Free with attribution

**Incompetech**
- Royalty-free music by Kevin MacLeod
- Genres include orchestral, world music
- Free with attribution

**Free Music Archive**
- Large collection
- Various licenses (check each)
- Curated selections

**BBC Sound Effects**
- 16,000+ effects
- Free for personal/educational
- High quality

---

#### 3D Assets

**Poly Haven**
- HDRIs, textures, 3D models
- CC0 (public domain)
- High quality
- polyhaven.com

**Sketchfab Free Models**
- Filter by "Downloadable" + "Free"
- CC licenses
- Game-ready models
- sketchfab.com

**OpenGameArt**
- Game-specific assets
- Various licenses
- Community-driven
- opengameart.org

**BlendSwap**
- Blender files
- Free models
- Rigged characters
- blend-swap.com

---

### 9. WRITING & DIALOGUE

#### Claude (Free Tier) ⭐ YOU'RE USING IT

**Website:** claude.ai
**Cost:** FREE tier available

**Features:**
- Long context (200K tokens)
- Excellent creative writing
- Dialogue generation
- Quest design
- Shahnameh adaptation

**Usage:**
```
Prompt: "Adapt the battle between Rostam and the lion from
Shahnameh into a 3-act boss fight sequence with dialogue and
player choices. Keep epic poetry tone but make interactive."
```

---

#### ChatGPT (Free Tier)

**Website:** chat.openai.com
**Cost:** FREE tier (GPT-3.5)

**Use For:**
- Brainstorming
- Alternative perspectives
- Quick content generation

---

### 10. PROCEDURAL GENERATION

#### Houdini Apprentice - FREE (Non-Commercial)

**Website:** sidefx.com
**Cost:** FREE for non-commercial

**Features:**
- Procedural 3D generation
- Environment creation
- VFX tools
- Game engine integration

**Use For:**
- Procedural environments
- Rock formations
- Vegetation placement
- Complex effects

---

### 11. ADDITIONAL FREE TOOLS

#### DaVinci Resolve - FREE VIDEO EDITING

**Use For:**
- Trailers
- Dev diaries
- Marketing videos

#### OBS Studio - FREE SCREEN RECORDING

**Use For:**
- Gameplay recording
- Development streams
- Tutorials

#### Git & GitHub - FREE VERSION CONTROL

**Use For:**
- Code management
- Collaboration
- Backup

---

## Recommended Minimal Setup (100% Free)

### For 3D Game (Unreal Path):

1. **Unreal Engine 5** - Game engine
2. **Blender** - 3D modeling
3. **Mixamo** - Character rigging/animation
4. **Quixel Megascans** - Environment assets (free with UE5)
5. **Stable Diffusion (local)** - Concept art
6. **AudioCraft** - Music/SFX generation
7. **Bark/XTTS** - Voice
8. **Audacity** - Audio editing
9. **Krita** - UI design
10. **Claude Free** - Writing/design

**Total Cost: $0/month**

---

### For 3D Game (Godot Path):

1. **Godot Engine** - Game engine
2. **Blender** - 3D modeling
3. **Mixamo** - Character rigging/animation
4. **Poly Haven** - Textures/HDRIs
5. **Stable Diffusion (local)** - Concept art
6. **AudioCraft** - Music/SFX generation
7. **Bark/XTTS** - Voice
8. **Audacity** - Audio editing
9. **Krita** - UI design
10. **Claude Free** - Writing/design

**Total Cost: $0/month**

---

## Hardware Requirements

### Minimum for AI Tools (Local):

- **GPU:** NVIDIA RTX 2060 or better (6GB+ VRAM)
- **RAM:** 16GB
- **Storage:** 100GB+ SSD (for AI models + game dev)
- **CPU:** Modern quad-core+

### Optimal:

- **GPU:** RTX 3060+ (12GB VRAM)
- **RAM:** 32GB
- **Storage:** 500GB+ NVMe SSD
- **CPU:** 6-8 core

---

## On-Demand Paid Options (Only If Necessary)

### When Free Tools Aren't Sufficient:

**ElevenLabs (Voice)**
- Free: 10,000 chars/month
- Paid: $5/month for 30,000 chars
- **Use if:** Bark/XTTS quality insufficient

**Meshy.ai (3D Generation)**
- Free: Limited credits/month
- Paid: $20/month
- **Use if:** Blender modeling too time-consuming

**Midjourney (Concept Art)**
- No free tier
- Paid: $10/month basic
- **Use if:** Stable Diffusion results unsatisfactory

---

## Workflow: Complete Free Pipeline

### Character Creation (100% Free):

```
1. Concept: Stable Diffusion (local)
   ↓
2. 3D Model: Blender (manual modeling) or MB-Lab add-on
   ↓
3. Rigging: Mixamo auto-rig or Blender Rigify
   ↓
4. Animation: Mixamo library + Blender custom
   ↓
5. Textures: Blender texture painting or ArmorPaint
   ↓
6. Voice: Record team member → XTTS clone variations
   ↓
7. Import to game engine
```

### Environment Creation (100% Free):

```
1. Concept: Stable Diffusion (local)
   ↓
2. Blockout: Game engine primitives
   ↓
3. Assets: Poly Haven + Blender custom models
   ↓
4. Textures: Poly Haven PBR materials
   ↓
5. Lighting: Engine-specific (Lumen for UE5, GI for Godot)
   ↓
6. Polish: Detail pass
```

### Audio Creation (100% Free):

```
Music:
1. Generate themes with AudioCraft
2. Layer and arrange in Audacity
3. Mix with Freesound.org ambiences

Voice:
1. Record short samples from team
2. Clone with XTTS
3. Generate dialogue
4. Clean in Audacity

SFX:
1. Generate with AudioCraft AudioGen
2. Supplement with Freesound.org
3. Edit in Audacity
```

---

## Tips for Maximum Free Tool Efficiency

1. **Batch Processing**
   - Generate many variations at once
   - Use overnight for long AI processes

2. **Community Assets First**
   - Check free asset libraries before creating
   - Modify existing assets vs. create from scratch

3. **Procedural When Possible**
   - Blender Geometry Nodes for repetitive assets
   - Houdini Apprentice for complex generation

4. **Reuse and Variation**
   - Create base assets, make variations
   - Texture swaps for different characters

5. **Learn the Tools Deeply**
   - Master Blender (replaces many paid tools)
   - Understand Stable Diffusion prompting
   - Explore free asset sites regularly

---

## Avoiding Paid Traps

**Don't Pay For:**
- ❌ Asset marketplace packs (use free libraries first)
- ❌ Stock music (use AudioCraft + Freesound)
- ❌ Code tools (Claude Code handles coding)
- ❌ Tutorials (YouTube + official docs are free)
- ❌ Cloud AI credits (run locally when possible)

**Only Pay For:**
- ✅ Extremely high-quality voice (if Bark/XTTS insufficient)
- ✅ Critical 3D models (if team can't model in time)
- ✅ Professional music (only for trailer/marketing)

---

## Learning Resources (All Free)

### Blender:
- Blender Guru (YouTube)
- Grant Abbitt (YouTube)
- Official Blender documentation

### Unreal Engine:
- Official Epic Games learning portal
- Unreal Sensei (YouTube)
- Matt Aspland (YouTube)

### Godot:
- Official Godot docs (in this repo!)
- GDQuest (YouTube)
- Heartbeast (YouTube)

### Stable Diffusion:
- /r/StableDiffusion (Reddit)
- Civitai tutorials
- AUTOMATIC1111 wiki

### Game Design:
- Game Maker's Toolkit (YouTube)
- Extra Credits (YouTube)
- GDC talks (YouTube)

---

**Remember: A 2-person team with Claude Code + free AI tools can match the output of a larger team using traditional pipelines. The limitation is time, not money.**
