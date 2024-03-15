import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Terminal Framework",
  description: "A Cool Framework To Create A Terminal Interfaces",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/add_text' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'GET STARTED', link: '/get_started' },
          { text: 'add_text', link: '/add_text' },
          { text: 'add_colored_text', link: '/add_colored_text' },
          { text: 'display_options', link: '/display_options' },
          { text: 'check_box', link: '/check_box' },
          { text: 'get_user_input', link: '/get_user_input'},
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/noone313' }
    ]
  }
})
