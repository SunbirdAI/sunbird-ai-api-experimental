/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./front_end/*.{html,js}"],
  theme: {
    extend: {},
    backgroundSize: {
      'auto': 'auto',
      'cover': 'cover',
      'contain': 'contain',
      '50%': '50%',
      '16': '4rem',
    },
    container:{
      center:true,
    }
  },
  plugins: [],
}

