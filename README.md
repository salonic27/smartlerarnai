# smartlearn ai 🧠

A multimodal machine learning learning assistant powered by generative AI. Smart Learn AI provides four distinct learning modes: text explanations, runnable code examples, audio lessons, and educational visualizations.

## Features

### 🔤 Text Explanation
- Comprehensive explanations of ML concepts
- Adjustable depth levels (beginner, intermediate, advanced)
- Clear learning objectives for each topic
- Markdown-formatted content for easy reading

### 💻 Code Generator
- Generate complete, runnable Python code examples
- Includes comprehensive comments and documentation
- Google Colab integration for instant execution
- Downloadable code files
- Time complexity specifications


### 🎧 Audio Lesson
- Browser-based text-to-speech audio lessons
- Three length options (short, medium, long)
- Play, pause, and stop controls
- Full lesson transcripts included
- Conversational teaching style
### 🖼️ Image Generator
- Educational diagrams and visualizations
- Multiple style options (technical diagram, flowchart, infographic, etc.)
- High-quality reference images
- Direct image downloads

## Tech Stack

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **React Router** - Client-side routing
- **Vite** - Build tool and dev server
- **Lucide React** - Icon library
- **React Markdown** - Markdown rendering

### Backend
- **Supabase Edge Functions** - Serverless API endpoints
- **Supabase Database** - PostgreSQL with Row Level Security
- **Deno** - Edge function runtime

### AI Integration
- **Google Gemini API** - Text and code generation (optional)
- **Browser Speech Synthesis** - Text-to-speech (built-in)
- **Pexels** - Educational reference images (fallback)

## Quick Start

### 1. Clone and Install

```bash
npm install
```

### 2. Environment Setup

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

The Supabase environment variables are already configured. For demo mode, no additional setup is needed.

### 3. Optional: Add Gemini API Key

To enable real AI generation (not required for demo):

1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add to your `.env` file:
   ```
   GEMINI_API_KEY=your-api-key-here
   DEMO_MODE=false
   ```

### 4. Run the Application

```bash
npm run dev
```

The app will be available at the URL shown in your terminal.

## 5-Minute Demo Script

### Step 1: Homepage Overview (30 seconds)
- Navigate to homepage
- Show four feature cards
- Highlight the quick start guide

### Step 2: Text Explanation (1 minute)
1. Click "Text Explanation"
2. Enter topic: **"backpropagation"**
3. Select depth: **"intermediate"**
4. Click "Generate Explanation"
5. Show:
   - Learning objectives
   - Comprehensive markdown content
   - Proper formatting and structure

### Step 3: Code Generator (1.5 minutes)
1. Click "Code Generator"
2. Enter algorithm: **"neural network from scratch"**
3. Select complexity: **"O(n)"**
4. Click "Generate Code"
5. Demonstrate:
   - Syntax-highlighted code display
   - Download button functionality
   - "Open in Colab" button
   - Run instructions

### Step 4: Audio Lesson (1.5 minutes)
1. Click "Audio Lesson"
2. Enter topic: **"deep learning"**
3. Select length: **"medium"**
4. Click "Generate Audio Lesson"
5. Show:
   - Play/pause/stop controls
   - Audio playback using browser TTS
   - Full lesson transcript
   - Duration estimate

### Step 5: Image Generator (1 minute)
1. Click "Image Generator"
2. Enter concept: **"CNN architecture"**
3. Select style: **"technical diagram"**
4. Click "Generate Images"
5. Display:
   - Multiple generated images
   - Descriptive captions
   - Download/open options

### Step 6: Wrap-up (30 seconds)
- Navigate back to homepage
- Summarize multimodal learning approach
- Mention production-ready features (RLS, API design, etc.)

## Architecture

### Frontend Structure
```
src/
├── components/
│   └── Layout.tsx          # Main layout with navigation
├── pages/
│   ├── HomePage.tsx        # Landing page
│   ├── ExplainPage.tsx     # Text explanation feature
│   ├── CodePage.tsx        # Code generation feature
│   ├── AudioPage.tsx       # Audio lesson feature
│   └── ImagePage.tsx       # Image generation feature
├── lib/
│   └── supabase.ts         # Supabase client & API calls
├── App.tsx                 # Router configuration
└── main.tsx                # Application entry point
```

### Backend Structure
```
supabase/
└── functions/
    ├── explain/            # Text explanation endpoint
    ├── code/               # Code generation endpoint
    ├── audio/              # Audio lesson endpoint
    └── image/              # Image generation endpoint
```

### Database Schema
- `learning_sessions` - User session tracking
- `generated_content` - Content history and caching

## API Endpoints

All endpoints are deployed as Supabase Edge Functions:

### POST /explain
Generate text explanations of ML concepts.

**Request:**
```json
{
  "topic": "backpropagation",
  "depth": "intermediate"
}
```

**Response:**
```json
{
  "success": true,
  "topic": "backpropagation",
  "explanation": "# Backpropagation\n\n...",
  "learningObjectives": ["..."],
  "source": "gemini"
}
```

### POST /code
Generate runnable code examples.

**Request:**
```json
{
  "algorithm": "neural network from scratch",
  "complexity": "O(n)",
  "language": "python"
}
```

**Response:**
```json
{
  "success": true,
  "algorithm": "neural network from scratch",
  "code": "import numpy as np...",
  "colabLink": "https://colab.research.google.com/...",
  "runInstructions": "1. Save to a .py file..."
}
```

### POST /audio
Generate audio lesson scripts.

**Request:**
```json
{
  "topic": "deep learning",
  "length": "medium"
}
```

**Response:**
```json
{
  "success": true,
  "topic": "deep learning",
  "script": "Welcome to this lesson on deep learning...",
  "duration": 240,
  "useBrowserTTS": true
}
```

### POST /image
Generate educational images.

**Request:**
```json
{
  "concept": "CNN architecture",
  "style": "technical diagram"
}
```

**Response:**
```json
{
  "success": true,
  "concept": "CNN architecture",
  "images": [
    {
      "url": "https://...",
      "description": "Visualization of CNN architecture..."
    }
  ]
}
```

## Demo Mode vs Production Mode

### Demo Mode (Default)
- Uses mock/generated content
- No API keys required
- Instant responses
- Perfect for demos and development

### Production Mode
- Requires `GEMINI_API_KEY`
- Set `DEMO_MODE=false` in `.env`
- Real AI-generated content
- Higher quality, contextual responses

## Security Features

- **Row Level Security (RLS)** enabled on all database tables
- **CORS headers** properly configured on all endpoints
- **Input validation** on all API endpoints
- **No secrets in client code** - all API keys server-side
- **Rate limiting** considerations in place

## Future Enhancements

- [ ] User authentication and saved sessions
- [ ] Content history dashboard
- [ ] Real-time collaboration features
- [ ] Stable Diffusion integration for custom images
- [ ] Advanced code sandbox for safe execution
- [ ] Learning path recommendations
- [ ] Progress tracking and analytics
- [ ] Export to PDF/presentation formats
- [ ] Mobile app version

## Testing

### Quick Test
Run the demo script above to verify all features work end-to-end.

### Manual Testing Checklist
- [ ] Homepage loads with all navigation links
- [ ] Text explanation generates and displays markdown
- [ ] Code generator produces valid Python code
- [ ] Download button works for code
- [ ] Google Colab link is generated
- [ ] Audio lesson plays in browser
- [ ] Play/pause controls work correctly
- [ ] Images load and display properly
- [ ] All error states display correctly
- [ ] Responsive design works on mobile

## Build for Production

```bash
npm run build
```

The optimized production build will be in the `dist/` folder.

## Known Limitations

1. **Code Execution**: Code samples are downloadable but not executed in-browser for security
2. **Image Generation**: Currently uses placeholder images; integrate Stable Diffusion for custom generation
3. **Audio Quality**: Uses browser TTS; consider ElevenLabs or gTTS for production
4. **Session Persistence**: Sessions are tracked but history features are minimal

## Troubleshooting

### "Missing Supabase environment variables"
- Ensure `.env` file exists with proper Supabase credentials
- Check that variables start with `VITE_` for Vite to pick them up

### Edge functions not responding
- Verify functions are deployed: Check Supabase dashboard
- Check CORS headers if getting network errors
- Ensure DEMO_MODE is set correctly

### Audio not playing
- Verify browser supports Speech Synthesis API
- Try a different browser (Chrome/Edge recommended)
- Check browser audio permissions

## Contributing

This is a hackathon MVP. For production use:
1. Add comprehensive error handling
2. Implement proper rate limiting
3. Add user authentication
4. Set up monitoring and logging
5. Add unit and integration tests
6. Implement caching strategies

## License

MIT License - feel free to use for educational purposes.

## Support

For issues or questions, check the inline code comments or refer to:
- [Supabase Documentation](https://supabase.com/docs)
- [React Documentation](https://react.dev)
- [Google Gemini API](https://ai.google.dev/docs)

---

**Built with ❤️ for hackathon demo - Smart Learn AI Team**
