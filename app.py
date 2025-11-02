import streamlit as st
import pandas as pd
from typing import List, Dict, Optional

# Page Configuration
st.set_page_config(
    page_title="Vinyl Verse | Curate Your Soundscape",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# Custom CSS for Aesthetic Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap');
    
    /* Main Theme Colors */
    :root {
        --primary-black: #0A0A0A;
        --deep-grey: #1A1A1A;
        --gold: #D4AF37;
        --silver: #C0C0C0;
        --accent-grey: #2A2A2A;
    }
    
    /* Global Styles */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    
    /* Mobile Responsive */
    @media (max-width: 768px) {
        .banner-title {
            font-size: 2.5rem !important;
        }
        
        .banner-subtitle {
            font-size: 1rem !important;
        }
        
        .banner-container {
            padding: 2rem 1rem !important;
        }
        
        .product-card {
            margin-bottom: 1rem !important;
            padding: 1rem !important;
        }
        
        .product-image {
            height: 200px !important;
        }
        
        .detail-image {
            max-height: 400px !important;
        }
        
        .main .block-container {
            padding: 0.5rem !important;
        }
        
        .cart-badge {
            top: 10px !important;
            right: 10px !important;
            padding: 0.5rem 1rem !important;
            font-size: 0.9rem !important;
        }
    }
    
    @media (max-width: 480px) {
        .banner-title {
            font-size: 2rem !important;
        }
        
        .product-name {
            font-size: 1.1rem !important;
        }
        
        .product-price {
            font-size: 1.3rem !important;
        }
    }
    
    /* Banner Styling */
    .banner-container {
        background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #2A2A2A 100%);
        padding: 4rem 2rem;
        margin-bottom: 3rem;
        border-bottom: 3px solid #D4AF37;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
    }
    
    .banner-title {
        font-family: 'Playfair Display', serif;
        font-size: 4.5rem;
        font-weight: 900;
        color: #D4AF37;
        margin: 0;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.9);
        letter-spacing: 2px;
    }
    
    .banner-subtitle {
        font-family: 'Roboto', sans-serif;
        font-size: 1.5rem;
        color: #C0C0C0;
        margin-top: 1rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    /* Product Card Styling */
    .product-card {
        background: linear-gradient(145deg, #1A1A1A 0%, #0A0A0A 100%);
        border: 2px solid #2A2A2A;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.6);
        cursor: pointer;
    }
    
    .product-card:hover {
        border-color: #D4AF37;
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(212, 175, 55, 0.3);
    }
    
    .product-image {
        width: 100%;
        height: 280px;
        object-fit: cover;
        border-radius: 8px;
        border: 2px solid #2A2A2A;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .product-image:hover {
        transform: scale(1.05);
    }
    
    .product-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: #D4AF37;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .product-price {
        font-family: 'Roboto', sans-serif;
        font-size: 1.8rem;
        color: #C0C0C0;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem 0.3rem 0.3rem 0;
    }
    
    .badge-gold {
        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 100%);
        color: #0A0A0A;
    }
    
    .badge-platinum {
        background: linear-gradient(135deg, #C0C0C0 0%, #E5E4E2 100%);
        color: #0A0A0A;
    }
    
    .badge-genre {
        background: #2A2A2A;
        color: #C0C0C0;
        border: 1px solid #3A3A3A;
    }
    
    .badge-clickable {
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .badge-clickable:hover {
        transform: scale(1.1);
        box-shadow: 0 4px 8px rgba(212, 175, 55, 0.4);
    }
    
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .badge-button {
        background: transparent;
        border: none;
        padding: 0;
        cursor: pointer;
    }
    
    /* Cart Badge */
    .cart-badge {
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 100%);
        color: #0A0A0A;
        padding: 0.8rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.5);
        z-index: 999;
        border: 2px solid #0A0A0A;
    }
    
    /* Detail View Styling */
    .detail-container {
        background: linear-gradient(145deg, #1A1A1A 0%, #0A0A0A 100%);
        border: 2px solid #D4AF37;
        border-radius: 16px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 12px 32px rgba(212, 175, 55, 0.2);
    }
    
    .detail-image {
        width: 100%;
        height: 500px;
        object-fit: cover;
        border-radius: 12px;
        border: 3px solid #D4AF37;
    }
    
    .detail-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: #D4AF37;
        margin-bottom: 1rem;
    }
    
    .detail-description {
        font-family: 'Roboto', sans-serif;
        color: #C0C0C0;
        font-size: 1.1rem;
        line-height: 1.8;
        margin: 1.5rem 0;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 100%);
        color: #0A0A0A;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 2rem;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 16px rgba(212, 175, 55, 0.4);
    }
    
    /* Badge Button Styling - Genre/Aesthetic badges */
    div[data-testid*="badge_genre"] button,
    div[data-testid*="badge_aesthetic"] button {
        background: #2A2A2A !important;
        color: #C0C0C0 !important;
        border: 1px solid #3A3A3A !important;
        border-radius: 20px !important;
        padding: 0.3rem 0.8rem !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        margin: 0.2rem 0 !important;
    }
    
    div[data-testid*="badge_genre"] button:hover,
    div[data-testid*="badge_aesthetic"] button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 4px 8px rgba(212, 175, 55, 0.4) !important;
        border-color: #D4AF37 !important;
    }
    
    /* Badge Button Styling - Replica badges (Gold) */
    div[data-testid*="badge_replica"] button {
        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 100%) !important;
        color: #0A0A0A !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.3rem 0.8rem !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        margin: 0.2rem 0 !important;
    }
    
    div[data-testid*="badge_replica"] button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 4px 8px rgba(212, 175, 55, 0.5) !important;
    }
    
    /* Style buttons containing "Platinum" */
    button:contains("Platinum") {
        background: linear-gradient(135deg, #C0C0C0 0%, #E5E4E2 100%) !important;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #0A0A0A;
    }
    
    .stSelectbox label, .stSlider label, .stMultiSelect label {
        color: #D4AF37 !important;
        font-weight: 700 !important;
        font-family: 'Roboto', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile Sidebar */
    @media (max-width: 768px) {
        .css-1d391kg {
            width: 100% !important;
        }
        
        [data-testid="stSidebar"] {
            width: 100% !important;
        }
        
        .stButton > button {
            font-size: 0.9rem !important;
            padding: 0.5rem 1rem !important;
        }
    }
    
    /* Better button styling */
    .stButton > button {
        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 100%) !important;
        color: #0A0A0A !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 16px rgba(212, 175, 55, 0.4) !important;
    }
    
    /* Improve text readability */
    p, div, span {
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    </style>
""", unsafe_allow_html=True)

# Mock Product Catalog
PRODUCT_CATALOG = [
    {
        "id": 101,
        "album_title": "The Wall",
        "artist": "Pink Floyd",
        "genre": "Rock & Roll",
        "aesthetic": "Industrial Grunge",
        "price": 4999,
        "is_replica": True,
        "replica_type": "Platinum",
        "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800&h=800&fit=crop&q=80",
        "description": "A masterful tribute to Pink Floyd's iconic rock opera masterpiece. Features riveted metal frame with aged patina finish, industrial grunge aesthetic that captures the raw energy of rock history.",
        "album_facts": "🔥 INSANE FACTS: Released in 1979, 'The Wall' sold over 30 million copies worldwide and achieved 23x Platinum certification! The album spent 15 weeks at #1 on Billboard 200. The tour featured a 40-foot-high wall built during performances. Roger Waters wrote most songs dealing with isolation and abandonment - themes from his own life. 'Another Brick in the Wall, Part 2' was banned in South Africa for its anti-authoritarian message!"
    },
    {
        "id": 102,
        "album_title": "Abbey Road",
        "artist": "The Beatles",
        "genre": "Rock & Roll",
        "aesthetic": "Golden Replica",
        "price": 8999,
        "is_replica": True,
        "replica_type": "Gold",
        "image_url": "https://images.unsplash.com/photo-1571974599782-87624638275c?w=800&h=800&fit=crop&q=80",
        "description": "Prestigious golden replica celebrating The Beatles' timeless masterpiece. Crafted with premium gold leaf accents and museum-quality framing, honoring the Fab Four's final recorded album.",
        "album_facts": "🎸 LEGENDARY FACTS: Released in 1969, 'Abbey Road' sold over 12 million copies and achieved 12x Platinum! The iconic zebra crossing photo took only 10 minutes to shoot. Paul McCartney is barefoot in the cover photo - a rumor started that he was dead! The album's medley (sides 2) was revolutionary - no band had done that before. 'Come Together' was written for Timothy Leary's campaign slogan. The album spent 11 weeks at #1 and is considered one of the greatest albums ever!"
    },
    {
        "id": 103,
        "album_title": "Thriller",
        "artist": "Michael Jackson",
        "genre": "Pop",
        "aesthetic": "Golden Replica",
        "price": 7999,
        "is_replica": True,
        "replica_type": "Platinum",
        "image_url": "https://images.unsplash.com/photo-1515169067868-5387ec356754?w=800&h=800&fit=crop&q=80",
        "description": "Platinum-certified replica of the best-selling album of all time. Features silver platinum accents and elegant minimalist design, celebrating the King of Pop's monumental achievement.",
        "album_facts": "⭐ MIND-BLOWING FACTS: Released in 1982, 'Thriller' sold over 100 MILLION copies worldwide - THE BEST-SELLING ALBUM OF ALL TIME! It spent 37 weeks at #1 on Billboard 200. The album won 8 Grammy Awards including Album of the Year. Vincent Price's spoken word on 'Thriller' was recorded in one take! The music video for 'Thriller' was 14 minutes long and cost $500,000 - revolutionary at the time. Seven of the nine tracks became top 10 singles. Michael Jackson's moonwalk debuted during the Motown 25 performance promoting this album!"
    },
    {
        "id": 104,
        "album_title": "Symphony No. 40",
        "artist": "Mozart",
        "genre": "Classical",
        "aesthetic": "Royal Velvet",
        "price": 6999,
        "is_replica": False,
        "replica_type": None,
        "image_url": "https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=800&h=800&fit=crop",
        "description": "Classical elegance meets modern artistry. Velvet-lined frame with ornate gold detailing, perfect for displaying classical masterpieces in regal fashion.",
        "album_facts": "🎼 CLASSICAL MASTERPIECE: Composed in 1788, Mozart's Symphony No. 40 in G minor is one of only two symphonies he wrote in minor keys. Written in just 6 weeks alongside Symphonies 39 and 41! The work wasn't performed during Mozart's lifetime - it was discovered after his death. It's considered one of the greatest symphonies ever written. The first movement's opening is instantly recognizable and has been featured in countless films. This symphony represents the pinnacle of Classical era composition!"
    },
    {
        "id": 105,
        "album_title": "Bollywood Classics",
        "artist": "RD Burman",
        "genre": "Indian Custom",
        "aesthetic": "Golden Replica",
        "price": 5999,
        "is_replica": True,
        "replica_type": "Gold",
        "image_url": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=800&h=800&fit=crop",
        "description": "A tribute to Indian cinema's golden era. Custom-designed golden replica with intricate patterns inspired by Indian artistry, honoring the legendary music director.",
        "album_facts": "🎬 BOLLYWOOD LEGEND: RD Burman revolutionized Indian film music with over 331 films! Known as 'Pancham Da', he introduced western instruments to Bollywood. His compositions blend Indian classical with jazz, rock, and Latin music. Created iconic soundtracks for films like 'Sholay', 'Amar Prem', and 'Caravan'. His innovative use of the mouth organ and synthesiser was groundbreaking. RD Burman's music continues to inspire generations - many modern songs sample his compositions!"
    },
    {
        "id": 106,
        "album_title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "genre": "Rock & Roll",
        "aesthetic": "Industrial Grunge",
        "price": 6499,
        "is_replica": False,
        "replica_type": None,
        "image_url": "https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?w=800&h=800&fit=crop",
        "description": "Industrial grunge aesthetic with dark metal textures and riveted edges. Captures the essence of progressive rock's most iconic album.",
        "album_facts": "🌙 PHENOMENAL FACTS: Released in 1973, 'The Dark Side of the Moon' sold over 45 million copies worldwide! It spent 741 weeks (over 14 YEARS!) on Billboard 200 - the longest chart run in history! The album stayed on charts for 900+ weeks total. The prism design on the cover represents light and dark themes. The album explores themes of mental illness, greed, time, and death. 'Time' features actual alarm clocks recorded by the band. The heartbeat sound throughout was created by Roger Waters' heartbeat. It's been certified 15x Platinum in the US alone!"
    },
    {
        "id": 107,
        "album_title": "A Night at the Opera",
        "artist": "Queen",
        "genre": "Rock & Roll",
        "aesthetic": "Royal Velvet",
        "price": 7499,
        "is_replica": True,
        "replica_type": "Gold",
        "image_url": "https://images.unsplash.com/photo-1509824227185-9c5a01ceba0d?w=800&h=800&fit=crop&q=80",
        "description": "Regal presentation fit for rock royalty. Velvet-lined frame with golden crown motifs and ornate detailing, celebrating Queen's operatic masterpiece.",
        "album_facts": "👑 ROYAL FACTS: Released in 1975, 'A Night at the Opera' sold over 10 million copies worldwide! It was the most expensive album ever recorded at the time - costing £40,000 (equivalent to £500,000 today)! 'Bohemian Rhapsody' took 3 weeks to record with 180 vocal overdubs. The song was initially rejected by record executives but became Queen's first #1 hit. The album features 'God Save the Queen' played on a harmonium. Freddie Mercury wrote 'Bohemian Rhapsody' in his head - no sheet music. The album's title references the Marx Brothers film. It's been certified 4x Platinum!"
    },
    {
        "id": 108,
        "album_title": "Classical Collection",
        "artist": "Various Artists",
        "genre": "Classical",
        "aesthetic": "Minimalist",
        "price": 4499,
        "is_replica": False,
        "replica_type": None,
        "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800&h=800&fit=crop",
        "description": "Clean lines and elegant simplicity. Minimalist design that lets the music speak for itself, perfect for timeless classical compositions.",
        "album_facts": "🎹 TIMELESS ELEGANCE: This curated collection features masterpieces from Bach, Beethoven, Chopin, and Vivaldi. Classical music has been proven to enhance cognitive function and reduce stress. These compositions have stood the test of time for centuries. Each piece represents a different era of classical music evolution. Perfect for creating a sophisticated atmosphere in any space!"
    },
    {
        "id": 109,
        "album_title": "Led Zeppelin IV",
        "artist": "Led Zeppelin",
        "genre": "Rock & Roll",
        "aesthetic": "Industrial Grunge",
        "price": 8499,
        "is_replica": True,
        "replica_type": "Platinum",
        "image_url": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&h=800&fit=crop&q=80",
        "description": "Platinum-certified tribute to rock legends. Industrial design with aged metal textures and riveted frame, honoring the greatest rock album ever.",
        "album_facts": "⚡ EPIC ROCK FACTS: Released in 1971, 'Led Zeppelin IV' sold over 37 million copies worldwide! It's been certified 24x Platinum in the US alone! The album has no title - just four symbols representing each band member. 'Stairway to Heaven' is the most requested song on FM radio but was never released as a single! The album stayed on charts for 259 weeks. The cover art was discovered in an antique shop for £2.50. 'Black Dog' was named after a stray black labrador that wandered into the recording studio. 'When the Levee Breaks' features one of the most sampled drum beats in history!"
    },
    {
        "id": 110,
        "album_title": "Carnatic Masters",
        "artist": "MS Subbulakshmi",
        "genre": "Indian Custom",
        "aesthetic": "Golden Replica",
        "price": 5499,
        "is_replica": True,
        "replica_type": "Gold",
        "image_url": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=800&h=800&fit=crop",
        "description": "Celebrating Indian classical music heritage. Golden replica with traditional motifs and contemporary framing, honoring the Nightingale of India.",
        "album_facts": "🎵 CARNATIC LEGEND: MS Subbulakshmi was the first Indian musician to receive the Bharat Ratna (India's highest civilian award)! She performed at the UN General Assembly in 1966 - the first Indian to do so. Known as the 'Queen of Song', she sang in Tamil, Telugu, Sanskrit, Hindi, Bengali, and Malayalam. Her rendition of 'Suprabhatam' is played daily at temples across India. She performed for 6 hours non-stop at the age of 13! Her recording of 'Bhaja Govindam' sold over 1 million copies - unprecedented for classical music!"
    },
    {
        "id": 111,
        "album_title": "Kind of Blue",
        "artist": "Miles Davis",
        "genre": "Pop",
        "aesthetic": "Minimalist",
        "price": 5999,
        "is_replica": False,
        "replica_type": None,
        "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800&h=800&fit=crop",
        "description": "Sleek minimalist design reflecting the cool sophistication of jazz. Clean black frame with silver accents, celebrating the best-selling jazz album ever.",
        "album_facts": "🎺 JAZZ MASTERPIECE: Released in 1959, 'Kind of Blue' sold over 5 million copies - THE BEST-SELLING JAZZ ALBUM OF ALL TIME! It's been certified 5x Platinum. The entire album was recorded in just TWO sessions totaling 9 hours! Miles Davis gave minimal instructions to musicians - most tracks were first takes. The album pioneered modal jazz - a revolutionary approach. 'So What' became one of the most recognized jazz standards. Rolling Stone ranked it #12 on '500 Greatest Albums of All Time'. The album influenced countless musicians across genres!"
    },
    {
        "id": 112,
        "album_title": "La Bohème",
        "artist": "Puccini",
        "genre": "Classical",
        "aesthetic": "Royal Velvet",
        "price": 7999,
        "is_replica": False,
        "replica_type": None,
        "image_url": "https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=800&h=800&fit=crop",
        "description": "Opulent velvet-lined frame with gold leaf accents. A regal presentation for classical operatic masterpieces, honoring Puccini's timeless opera.",
        "album_facts": "🎭 OPERATIC GENIUS: Premiered in 1896, 'La Bohème' is one of the most performed operas worldwide! Puccini wrote the opera in just 4 months. The story is based on 'Scènes de la vie de bohème' by Henri Murger. The opera's 'Quando m'en vo' (Musetta's Waltz) is instantly recognizable. It inspired the hit musical 'Rent' and the film 'Moulin Rouge'. The opera has been performed over 1,000 times at the Metropolitan Opera alone! Puccini's emotional arias made him one of the most beloved opera composers. The opera's themes of love and sacrifice resonate across generations!"
    }
]

# Use curated Unsplash images for vinyl frames
# These images show actual vinyl records and frames

# Initialize Session State
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'gallery'
if 'filter_genre' not in st.session_state:
    st.session_state.filter_genre = None
if 'filter_aesthetic' not in st.session_state:
    st.session_state.filter_aesthetic = None
if 'filter_replica' not in st.session_state:
    st.session_state.filter_replica = None

def add_to_cart(product: Dict):
    """Add product to cart"""
    st.session_state.cart.append(product)
    st.success(f"✨ {product['album_title']} by {product['artist']} added to cart!")

def get_cart_count():
    """Get total items in cart"""
    return len(st.session_state.cart)

def filter_products(catalog: List[Dict], genres: List[str], aesthetics: List[str], price_range: tuple, replica_type: Optional[str] = None) -> List[Dict]:
    """Filter products based on selected criteria"""
    filtered = catalog.copy()
    
    if genres:
        filtered = [p for p in filtered if p['genre'] in genres]
    
    if aesthetics:
        filtered = [p for p in filtered if p['aesthetic'] in aesthetics]
    
    if replica_type:
        filtered = [p for p in filtered if p.get('is_replica') and p.get('replica_type') == replica_type]
    
    filtered = [p for p in filtered if price_range[0] <= p['price'] <= price_range[1]]
    
    return filtered

def apply_genre_filter(genre: str):
    """Apply genre filter from badge click"""
    st.session_state.filter_genre = genre
    st.session_state.view_mode = 'gallery'
    st.session_state.selected_product = None
    st.rerun()

def apply_aesthetic_filter(aesthetic: str):
    """Apply aesthetic filter from badge click"""
    st.session_state.filter_aesthetic = aesthetic
    st.session_state.view_mode = 'gallery'
    st.session_state.selected_product = None
    st.rerun()

def apply_replica_filter(replica_type: str):
    """Apply replica filter from badge click"""
    st.session_state.filter_replica = replica_type
    st.session_state.view_mode = 'gallery'
    st.session_state.selected_product = None
    st.rerun()

def render_banner():
    """Render the main banner"""
    st.markdown("""
        <div class="banner-container">
            <h1 class="banner-title">🎵 VINYL VERSE</h1>
            <p class="banner-subtitle">Curate Your Soundscape | The Vinyl Hall of Fame</p>
        </div>
    """, unsafe_allow_html=True)

def render_product_card(product: Dict, col):
    """Render a single product card"""
    with col:
        card_html = f"""
        <div class="product-card">
            <img src="{product['image_url']}" class="product-image" alt="{product['album_title']}" onerror="this.src='https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800&h=800&fit=crop&q=80'">
            <div style="color: #D4AF37; font-size: 1rem; margin-bottom: 0.3rem; font-weight: 600;">{product['artist']}</div>
            <div class="product-name">{product['album_title']}</div>
            <div class="product-price">₹{product['price']:,}</div>
        """
        card_html += "</div>"
        
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Clickable badges
        badge_cols = st.columns([1, 1, 1])
        badge_idx = 0
        
        if product['is_replica']:
            badge_class = "badge-gold" if product['replica_type'] == "Gold" else "badge-platinum"
            badge_text = f"⭐ {product['replica_type']} Replica"
            with badge_cols[badge_idx % 3]:
                if st.button(badge_text, key=f"badge_replica_{product['id']}", use_container_width=True):
                    apply_replica_filter(product['replica_type'])
            badge_idx += 1
        
        with badge_cols[badge_idx % 3]:
            if st.button(product['genre'], key=f"badge_genre_{product['id']}", use_container_width=True):
                apply_genre_filter(product['genre'])
        badge_idx += 1
        
        with badge_cols[badge_idx % 3]:
            if st.button(product['aesthetic'], key=f"badge_aesthetic_{product['id']}", use_container_width=True):
                apply_aesthetic_filter(product['aesthetic'])
        
        if st.button(f"Add to Cart 🛒", key=f"cart_{product['id']}", use_container_width=True):
            add_to_cart(product)
        
        if st.button(f"View Details 🔍", key=f"detail_{product['id']}", use_container_width=True):
            st.session_state.selected_product = product
            st.session_state.view_mode = 'detail'
            st.rerun()

def render_product_detail(product: Dict):
    """Render product detail view"""
    # Back to Gallery link
    if st.button("← Back to Gallery", key="back_to_gallery_top", use_container_width=False):
        st.session_state.view_mode = 'gallery'
        st.session_state.selected_product = None
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Two column layout: Image on left, details on right
    col_img, col_info = st.columns([1, 1])
    
    with col_img:
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="{product['image_url']}" class="detail-image" alt="{product['album_title']}" 
                     onerror="this.src='https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800&h=800&fit=crop&q=80'"
                     style="width: 100%; max-height: 600px; object-fit: cover; border-radius: 12px; border: 3px solid #D4AF37; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);">
            </div>
        """, unsafe_allow_html=True)
        
        # Custom design section
        st.markdown("""
            <div style="background: linear-gradient(145deg, #1A1A1A 0%, #0A0A0A 100%); 
                        border: 2px solid #D4AF37; border-radius: 12px; padding: 2rem; margin-top: 2rem;">
                <h3 style="color: #D4AF37; font-family: 'Playfair Display', serif; margin-bottom: 1rem;">
                    🎨 IN Design Your Own Masterpiece!
                </h3>
                <p style="color: #C0C0C0; line-height: 1.8;">
                    Customize this frame with any Indian artist, album, or style. We specialize in replicating Golden/Platinum records for the Indian market.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_info:
        st.markdown(f"""
            <div style="margin-bottom: 2rem;">
                <div class="detail-title">{product['album_title']}</div>
                <div style="color: #D4AF37; font-size: 1.5rem; margin-bottom: 1.5rem; font-weight: 600;">
                    {product['artist']}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Badges row
        st.markdown("### Click on any label to filter:")
        badge_cols = st.columns(4)
        
        if product['is_replica']:
            badge_text = f"⭐ {product['replica_type']} Replica"
            with badge_cols[0]:
                if st.button(badge_text, key=f"detail_badge_replica_{product['id']}", use_container_width=True):
                    apply_replica_filter(product['replica_type'])
        
        with badge_cols[1]:
            if st.button(product['genre'], key=f"detail_badge_genre_{product['id']}", use_container_width=True):
                apply_genre_filter(product['genre'])
        
        with badge_cols[2]:
            if st.button(product['aesthetic'], key=f"detail_badge_aesthetic_{product['id']}", use_container_width=True):
                apply_aesthetic_filter(product['aesthetic'])
        
        st.markdown("---")
        
        # Price
        st.markdown(f"""
            <div style="font-size: 2.5rem; color: #D4AF37; font-weight: 700; margin: 1.5rem 0;">
                ₹{product['price']:,}
            </div>
        """, unsafe_allow_html=True)
        
        # Description box
        st.markdown(f"""
            <div style="background: linear-gradient(145deg, #1A1A1A 0%, #0A0A0A 100%); 
                        border: 2px solid #2A2A2A; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;">
                <h4 style="color: #D4AF37; margin-bottom: 1rem; font-family: 'Playfair Display', serif;">Description</h4>
                <p style="color: #C0C0C0; line-height: 1.8; margin: 0;">
                    {product['description']}
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Aesthetic Deep Dive box
        features = get_aesthetic_features(product['aesthetic'])
        st.markdown(f"""
            <div style="background: linear-gradient(145deg, #1A1A1A 0%, #0A0A0A 100%); 
                        border: 2px solid #2A2A2A; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;">
                <h4 style="color: #D4AF37; margin-bottom: 1rem; font-family: 'Playfair Display', serif;">Aesthetic Deep Dive</h4>
                <p style="color: #C0C0C0; margin-bottom: 0.5rem;"><strong>Style:</strong> {product['aesthetic']}</p>
                <p style="color: #C0C0C0; margin: 0;"><strong>Features:</strong> {features}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Album Facts box
        if 'album_facts' in product and product['album_facts']:
            st.markdown(f"""
                <div style="background: linear-gradient(145deg, #1A1A1A 0%, #0A0A0A 100%); 
                            border: 2px solid #D4AF37; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;">
                    <h4 style="color: #D4AF37; margin-bottom: 1rem; font-family: 'Playfair Display', serif; font-size: 1.3rem;">
                        🎵 Album Facts & Trivia
                    </h4>
                    <p style="color: #C0C0C0; line-height: 1.8; margin: 0; font-size: 1rem;">
                        {product['album_facts']}
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛒 Add to Cart", use_container_width=True, type="primary"):
                add_to_cart(product)
        with col2:
            if st.button("← Back to Gallery", use_container_width=True):
                st.session_state.view_mode = 'gallery'
                st.session_state.selected_product = None
                st.rerun()

def get_aesthetic_features(aesthetic: str) -> str:
    """Get feature descriptions based on aesthetic"""
    features = {
        "Golden Replica": "Gold leaf accents, premium gilding, museum-quality certification",
        "Industrial Grunge": "Rivets, aged metal texture, weathered finish, industrial hardware",
        "Royal Velvet": "Velvet-lined interior, ornate gold detailing, regal crown motifs",
        "Minimalist": "Clean lines, sleek design, subtle silver accents, modern elegance"
    }
    return features.get(aesthetic, "Premium craftsmanship, custom framing")

# Main App
render_banner()

# Cart Badge
cart_count = get_cart_count()
if cart_count > 0:
    st.markdown(f'<div class="cart-badge">🛒 Cart ({cart_count})</div>', unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.markdown("## 🎛️ Filter Your Collection")
st.sidebar.markdown("---")

# Sync filters with badge clicks
default_genres = []
if st.session_state.filter_genre:
    default_genres = [st.session_state.filter_genre]

default_aesthetics = []
if st.session_state.filter_aesthetic:
    default_aesthetics = [st.session_state.filter_aesthetic]

# Genre Filter
genres = st.sidebar.multiselect(
    "🎵 Genre",
    options=["Rock & Roll", "Pop", "Classical", "Indian Custom"],
    default=default_genres
)

# Clear badge filter if sidebar filter changed
if genres != default_genres:
    st.session_state.filter_genre = None

# Aesthetic Filter
aesthetics = st.sidebar.multiselect(
    "🎨 Aesthetic",
    options=["Golden Replica", "Industrial Grunge", "Royal Velvet", "Minimalist"],
    default=default_aesthetics
)

# Clear badge filter if sidebar filter changed
if aesthetics != default_aesthetics:
    st.session_state.filter_aesthetic = None

# Replica Filter
replica_options = ["Gold", "Platinum"]
replica_default = []
if st.session_state.filter_replica:
    replica_default = [st.session_state.filter_replica]

replica_filter = st.sidebar.multiselect(
    "⭐ Replica Type",
    options=replica_options,
    default=replica_default
)

# Clear badge filter if sidebar filter changed
if replica_filter != replica_default:
    st.session_state.filter_replica = None

# Price Range Filter
price_range = st.sidebar.slider(
    "💰 Price Range (₹)",
    min_value=0,
    max_value=10000,
    value=(0, 10000),
    step=100
)

# Clear Filters Button
if st.sidebar.button("🔄 Clear All Filters"):
    st.session_state.filter_genre = None
    st.session_state.filter_aesthetic = None
    st.session_state.filter_replica = None
    st.rerun()

# Main Content Area
if st.session_state.view_mode == 'detail' and st.session_state.selected_product:
    render_product_detail(st.session_state.selected_product)
else:
    # Determine replica filter
    replica_type_filter = None
    if st.session_state.filter_replica:
        replica_type_filter = st.session_state.filter_replica
    elif replica_filter:
        replica_type_filter = replica_filter[0] if len(replica_filter) == 1 else None
    
    # Filter Products
    filtered_products = filter_products(PRODUCT_CATALOG, genres, aesthetics, price_range, replica_type_filter)
    
    # Display Results
    st.markdown(f"### 🎼 Found {len(filtered_products)} Masterpiece(s)")
    st.markdown("---")
    
    if filtered_products:
        # Display products in grid
        cols_per_row = 3
        for i in range(0, len(filtered_products), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                if i + j < len(filtered_products):
                    render_product_card(filtered_products[i + j], col)
    else:
        st.markdown("""
            <div style="text-align: center; padding: 4rem; color: #C0C0C0;">
                <h2 style="color: #D4AF37;">No products found</h2>
                <p>Try adjusting your filters to discover more masterpieces.</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #C0C0C0;">
        <p style="font-size: 1.1rem;">🎵 <strong>Vinyl Verse</strong> | Curate Your Soundscape</p>
        <p style="color: #666;">© 2024 The Replica Studio | Crafting Musical Legacies</p>
    </div>
""", unsafe_allow_html=True)

# JavaScript for styling badge buttons
st.markdown("""
    <script>
    // Style badge buttons based on their text content and context
    function styleBadgeButtons() {
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            const text = button.textContent || button.innerText || '';
            const buttonId = button.id || '';
            const buttonClass = button.className || '';
            
            // Skip main action buttons
            if (text.includes('Add to Cart') || text.includes('Back to Gallery') ||
                text.includes('View Details') || text.includes('Clear All Filters')) {
                return;
            }
            
            // Check if this is a badge button by looking for badge-related keys in various attributes
            const isBadgeButton = (
                buttonId.includes('badge') ||
                (text.match(/^(Rock & Roll|Pop|Classical|Indian Custom|Golden Replica|Industrial Grunge|Royal Velvet|Minimalist|Gold Replica|Platinum Replica|⭐.*Replica)$/i))
            );
            
            if (isBadgeButton && !text.includes('Cart') && !text.includes('Details')) {
                // Style genre badges
                if (text.match(/^(Rock & Roll|Pop|Classical|Indian Custom)$/i)) {
                    button.style.cssText = `
                        background: #2A2A2A !important;
                        color: #C0C0C0 !important;
                        border: 1px solid #3A3A3A !important;
                        border-radius: 20px !important;
                        padding: 0.3rem 0.8rem !important;
                        font-size: 0.85rem !important;
                        font-weight: 600 !important;
                        transition: all 0.2s ease !important;
                        margin: 0.2rem 0 !important;
                        cursor: pointer !important;
                        min-height: auto !important;
                        height: auto !important;
                    `;
                }
                // Style aesthetic badges
                else if (text.match(/^(Golden Replica|Industrial Grunge|Royal Velvet|Minimalist)$/i)) {
                    button.style.cssText = `
                        background: #2A2A2A !important;
                        color: #C0C0C0 !important;
                        border: 1px solid #3A3A3A !important;
                        border-radius: 20px !important;
                        padding: 0.3rem 0.8rem !important;
                        font-size: 0.85rem !important;
                        font-weight: 600 !important;
                        transition: all 0.2s ease !important;
                        margin: 0.2rem 0 !important;
                        cursor: pointer !important;
                        min-height: auto !important;
                        height: auto !important;
                    `;
                }
                // Style replica badges
                else if (text.includes('Platinum') || text.includes('⭐') && text.includes('Platinum')) {
                    button.style.cssText = `
                        background: linear-gradient(135deg, #C0C0C0 0%, #E5E4E2 100%) !important;
                        color: #0A0A0A !important;
                        border: none !important;
                        border-radius: 20px !important;
                        padding: 0.3rem 0.8rem !important;
                        font-size: 0.85rem !important;
                        font-weight: 600 !important;
                        transition: all 0.2s ease !important;
                        margin: 0.2rem 0 !important;
                        cursor: pointer !important;
                        min-height: auto !important;
                        height: auto !important;
                    `;
                }
                else if (text.includes('Gold') || (text.includes('⭐') && text.includes('Gold'))) {
                    button.style.cssText = `
                        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 100%) !important;
                        color: #0A0A0A !important;
                        border: none !important;
                        border-radius: 20px !important;
                        padding: 0.3rem 0.8rem !important;
                        font-size: 0.85rem !important;
                        font-weight: 600 !important;
                        transition: all 0.2s ease !important;
                        margin: 0.2rem 0 !important;
                        cursor: pointer !important;
                        min-height: auto !important;
                        height: auto !important;
                    `;
                }
            }
        });
    }
    
    // Run on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', styleBadgeButtons);
    } else {
        styleBadgeButtons();
    }
    
    // Run periodically to catch dynamically added buttons
    setInterval(styleBadgeButtons, 500);
    
    // Also run when DOM changes
    const observer = new MutationObserver(() => {
        setTimeout(styleBadgeButtons, 100);
    });
    observer.observe(document.body, { childList: true, subtree: true });
    </script>
""", unsafe_allow_html=True)

