/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/front_end/*.{html,js}"],
  theme: {
    extend: {
      aspectRatio: {
        '3/1': '3 / 1',
      }
    },
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

