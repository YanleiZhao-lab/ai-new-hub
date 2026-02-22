import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'AI News Hub',
  description: '每日 AI 新闻聚合平台',
  lang: 'zh-CN',
  base: '/',
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }],
    ['link', { rel: 'shortcut icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#3c8772' }]
  ],

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '最新资讯', link: '/news/' },
      { text: '行业动态', link: '/industry' },
      { text: '研究前沿', link: '/research' },
      { text: '热门推荐', link: '/trending' },
    ],

    sidebar: {
      '/': [
        {
          text: '核心板块',
          items: [
            { text: '行业动态', link: '/industry' },
            { text: '研究前沿', link: '/research' },
            { text: '热门推荐', link: '/trending' },
          ]
        }
      ],
      '/news/': [
        {
          text: '历史新闻',
          items: []
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ZhaoNancheng/ai-news-hub' }
    ],

    footer: {
      message: '基于 VitePress 构建',
      copyright: 'Copyright © 2026 AI News Hub'
    },

    search: {
      provider: 'local'
    }
  },

  markdown: {
    lineNumbers: true
  },

  // 忽略死链检查（动态生成的新闻页面）
  vite: {
    build: {
      rollupOptions: {
        onwarn(warning, warn) {
          // 忽略 dead link 警告
          if (warning.code === 'PLUGIN_WARN') return
          warn(warning)
        }
      }
    }
  },

  // 或者完全禁用死链检查
  ignoreDeadLinks: true
})
