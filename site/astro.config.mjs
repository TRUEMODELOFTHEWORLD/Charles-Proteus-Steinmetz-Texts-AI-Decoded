import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({
  site: 'https://truemodeloftheworld.github.io',
  base: '/Charles-Proteus-Steinmetz-Texts-AI-Decoded',
  integrations: [
    starlight({
      title: 'Steinmetz Decoded',
      description: 'A source-grounded research codex for Charles Proteus Steinmetz.',
      customCss: ['./src/styles/custom.css', 'katex/dist/katex.min.css'],
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/TRUEMODELOFTHEWORLD/Charles-Proteus-Steinmetz-Texts-AI-Decoded'
        }
      ],
      sidebar: [
        {
          label: 'Start Here',
          items: [
            { label: 'Who Was Steinmetz?', slug: 'who-was-steinmetz' },
            { label: 'Why Steinmetz Matters', slug: 'why-steinmetz-matters' }
          ]
        },
        {
          label: 'Source Library',
          items: [
            { label: 'Library Index', slug: 'source-library' },
            {
              label: 'Radiation, Light and Illumination',
              items: [
                { label: 'Book Overview', slug: 'sources/radiation-light-and-illumination' },
                { label: 'Lecture I', slug: 'sources/radiation-light-and-illumination/lecture-01' }
              ]
            },
            { label: 'Elementary Lectures', slug: 'sources/elementary-lectures-electric-discharges-waves-impulses' },
            { label: 'Engineering Mathematics', slug: 'sources/engineering-mathematics' },
            { label: 'Alternating Current Phenomena', slug: 'sources/theory-calculation-alternating-current-phenomena' },
            { label: 'Transient Electric Phenomena', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations' },
            { label: 'Theoretical Elements', slug: 'sources/theoretical-elements-electrical-engineering' },
            { label: 'Commonwealth Edison Trouble', slug: 'sources/commonwealth-edison-generating-system-trouble' }
          ]
        },
        {
          label: 'Concept Encyclopedia',
          items: [
            { label: 'Concept Index', slug: 'concepts' },
            { label: 'Radiation', slug: 'concepts/radiation' },
            { label: 'Electric Waves', slug: 'concepts/electric-waves' },
            { label: 'Ether', slug: 'concepts/ether' },
            { label: 'Illumination', slug: 'concepts/illumination' },
            { label: 'Transient Phenomena', slug: 'concepts/transient-phenomena' },
            { label: 'Symbolic Method', slug: 'concepts/symbolic-method' },
            { label: 'Hysteresis', slug: 'concepts/hysteresis' }
          ]
        },
        {
          label: 'Mathematics',
          items: [
            { label: 'Equation Catalog', slug: 'mathematics' },
            { label: 'Velocity, Frequency, Wavelength', slug: 'mathematics/equations/velocity-frequency-wavelength' }
          ]
        },
        {
          label: 'Archives',
          items: [
            { label: 'Diagram Archive', slug: 'diagrams' },
            { label: 'Glossary', slug: 'glossary' },
            { label: 'Hidden Gems', slug: 'hidden-gems' },
            { label: 'Research Questions', slug: 'research-questions' }
          ]
        },
        {
          label: 'Comparisons',
          items: [
            { label: 'Comparison Index', slug: 'comparisons' },
            { label: 'Steinmetz vs Modern EE', slug: 'comparisons/steinmetz-vs-modern-radiation' },
            { label: 'Tesla-Era Science', slug: 'comparisons/tesla-era-electrical-science' },
            { label: 'Ether-Field Reading Guide', slug: 'comparisons/ether-field-reading-guide' }
          ]
        },
        {
          label: 'Tools',
          items: [
            { label: 'Interactive Tools', slug: 'tools' }
          ]
        }
      ]
    }),
    mdx()
  ],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex]
  }
});
