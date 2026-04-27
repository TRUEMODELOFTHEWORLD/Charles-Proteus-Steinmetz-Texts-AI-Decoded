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
            { label: 'Project Tracker', slug: 'project-tracker' },
            { label: 'Publication Roadmap', slug: 'roadmap' },
            { label: 'Who Was Steinmetz?', slug: 'who-was-steinmetz' },
            { label: 'Why Steinmetz Matters', slug: 'why-steinmetz-matters' }
          ]
        },
        {
          label: 'Source Library',
          items: [
            { label: 'Library Index', slug: 'source-library' },
            { label: 'Processing Dashboard', slug: 'research-status' },
            {
              label: 'Radiation, Light and Illumination',
              items: [
                { label: 'Book Overview', slug: 'sources/radiation-light-and-illumination' },
                { label: 'Lecture I', slug: 'sources/radiation-light-and-illumination/lecture-01' }
              ]
            },
            { label: 'Elementary Lectures', slug: 'sources/elementary-lectures-electric-discharges-waves-impulses' },
            {
              label: 'Engineering Mathematics',
              items: [
                { label: 'Book Overview', slug: 'sources/engineering-mathematics' },
                { label: 'General Number', slug: 'sources/engineering-mathematics/general-number' }
              ]
            },
            {
              label: 'Alternating Current Phenomena',
              items: [
                { label: 'Book Overview', slug: 'sources/theory-calculation-alternating-current-phenomena' },
                { label: 'Symbolic Method', slug: 'sources/theory-calculation-alternating-current-phenomena/symbolic-method' },
                { label: 'Impedance And Reactance', slug: 'sources/theory-calculation-alternating-current-phenomena/impedance-reactance' },
                { label: 'Admittance', slug: 'sources/theory-calculation-alternating-current-phenomena/admittance-conductance-susceptance' }
              ]
            },
            {
              label: 'Transient Electric Phenomena',
              items: [
                { label: 'Book Overview', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations' },
                { label: 'Transient Terms', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations/transient-terms' },
                { label: 'Condenser Charge', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations/condenser-charge-discharge' },
                { label: 'Standing And Traveling Waves', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations/standing-traveling-waves' }
              ]
            },
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
            { label: 'Complex Quantities', slug: 'concepts/complex-quantities' },
            { label: 'Hysteresis', slug: 'concepts/hysteresis' },
            { label: 'Impedance', slug: 'concepts/impedance' },
            { label: 'Reactance', slug: 'concepts/reactance' },
            { label: 'Admittance', slug: 'concepts/admittance' },
            { label: 'Power Factor', slug: 'concepts/power-factor' },
            { label: 'Distributed Constants', slug: 'concepts/distributed-constants' },
            { label: 'Oscillation And Damping', slug: 'concepts/oscillation-damping' },
            { label: 'Inductance And Capacity', slug: 'concepts/inductance-capacity' }
          ]
        },
        {
          label: 'Mathematics',
          items: [
            { label: 'Equation Catalog', slug: 'mathematics' },
            { label: 'Velocity, Frequency, Wavelength', slug: 'mathematics/equations/velocity-frequency-wavelength' },
            { label: 'Symbolic Components', slug: 'mathematics/equations/symbolic-rectangular-components' },
            { label: 'Impedance And Reactance', slug: 'mathematics/equations/impedance-reactance' },
            { label: 'Admittance', slug: 'mathematics/equations/admittance-conductance-susceptance' },
            { label: 'Transient Term', slug: 'mathematics/equations/transient-term' },
            { label: 'RLC Oscillation', slug: 'mathematics/equations/rlc-oscillation' },
            { label: 'Condenser Oscillation', slug: 'mathematics/equations/condenser-oscillation-decrement' }
          ]
        },
        {
          label: 'Archives',
          items: [
            { label: 'Diagram Archive', slug: 'diagrams' },
            { label: 'Original RLI Figures', slug: 'diagrams/original-radiation-light-and-illumination' },
            { label: 'Original AC Figures', slug: 'diagrams/original-alternating-current-phenomena' },
            { label: 'Original Transient Figures', slug: 'diagrams/original-transient-electric-phenomena' },
            { label: 'Glossary', slug: 'glossary' },
            { label: 'Condensive Reactance', slug: 'glossary/condensive-reactance' },
            { label: 'Wattless Component', slug: 'glossary/wattless-component' },
            { label: 'Imaginary Unit j', slug: 'glossary/imaginary-unit-j' },
            { label: 'Electrostatic Capacity', slug: 'glossary/electrostatic-capacity' },
            { label: 'Counter EMF', slug: 'glossary/counter-electromotive-force' },
            { label: 'Effective Resistance', slug: 'glossary/effective-resistance' },
            { label: 'Hidden Gems', slug: 'hidden-gems' },
            { label: 'Research Questions', slug: 'research-questions' }
          ]
        },
        {
          label: 'Comparisons',
          items: [
            { label: 'Comparison Index', slug: 'comparisons' },
            { label: 'Steinmetz vs Modern EE', slug: 'comparisons/steinmetz-vs-modern-radiation' },
            { label: 'Modern AC Method', slug: 'comparisons/steinmetz-vs-modern-ac-symbolic-method' },
            { label: 'Tesla-Era Science', slug: 'comparisons/tesla-era-electrical-science' },
            { label: 'Tesla-Era Transients', slug: 'comparisons/transients-tesla-era-high-frequency' },
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
