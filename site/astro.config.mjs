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
      head: [
        {
          tag: 'script',
          attrs: {
            src: '/Charles-Proteus-Steinmetz-Texts-AI-Decoded/codex-ui.js',
            defer: true
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'theme-color',
            content: '#151b1c'
          }
        }
      ],
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
            { label: 'Why Steinmetz Matters', slug: 'why-steinmetz-matters' },
            { label: 'Source Library', slug: 'source-library' },
            { label: 'Processing Dashboard', slug: 'research-status' }
          ]
        },
        {
          label: 'Research Corpus',
          items: [
            { label: 'Bibliography Intake', slug: 'source-library/bibliography-intake' },
            { label: 'Steinmetz Patent Register', slug: 'sources/steinmetz-patents' },
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
            { label: 'General Lectures', slug: 'sources/general-lectures-electrical-engineering' },
            { label: 'Electric Apparatus', slug: 'sources/theory-calculation-electric-apparatus' },
            { label: 'America and the New Epoch', slug: 'sources/america-and-new-epoch' },
            { label: 'Relativity and Space', slug: 'sources/four-lectures-relativity-space' },
            { label: 'Commonwealth Edison Trouble', slug: 'sources/commonwealth-edison-generating-system-trouble' }
          ]
        },
        {
          label: 'Concept Encyclopedia',
          items: [
            { label: 'Concept Index', slug: 'concepts' },
            { label: 'Radiation', slug: 'concepts/radiation' },
            { label: 'Electric Waves', slug: 'concepts/electric-waves' },
            { label: 'Lightning And Surges', slug: 'concepts/lightning-surges' },
            { label: 'Ether', slug: 'concepts/ether' },
            { label: 'Illumination', slug: 'concepts/illumination' },
            { label: 'Transient Phenomena', slug: 'concepts/transient-phenomena' },
            { label: 'Symbolic Method', slug: 'concepts/symbolic-method' },
            { label: 'Complex Quantities', slug: 'concepts/complex-quantities' },
            { label: 'Hysteresis', slug: 'concepts/hysteresis' },
            { label: 'Harmonics And Wave Shape', slug: 'concepts/harmonics-wave-shape' },
            { label: 'Impedance', slug: 'concepts/impedance' },
            { label: 'Reactance', slug: 'concepts/reactance' },
            { label: 'Admittance', slug: 'concepts/admittance' },
            { label: 'Conductance', slug: 'concepts/conductance' },
            { label: 'Susceptance', slug: 'concepts/susceptance' },
            { label: 'Power Factor', slug: 'concepts/power-factor' },
            { label: 'Dielectric Loss', slug: 'concepts/dielectric-loss' },
            { label: 'Distributed Constants', slug: 'concepts/distributed-constants' },
            { label: 'Oscillation And Damping', slug: 'concepts/oscillation-damping' },
            { label: 'Inductance And Capacity', slug: 'concepts/inductance-capacity' }
          ]
        },
        {
          label: 'Mathematics And Tools',
          items: [
            { label: 'Equation Catalog', slug: 'mathematics' },
            { label: 'First Canonical Set', slug: 'mathematics/canonical-equation-canon' },
            { label: 'Velocity, Frequency, Wavelength', slug: 'mathematics/equations/velocity-frequency-wavelength' },
            { label: 'Symbolic Components', slug: 'mathematics/equations/symbolic-rectangular-components' },
            { label: 'Operator j', slug: 'mathematics/equations/symbolic-operator-j' },
            { label: 'Reactance Forms', slug: 'mathematics/equations/reactance-forms' },
            { label: 'Impedance And Reactance', slug: 'mathematics/equations/impedance-reactance' },
            { label: 'Admittance', slug: 'mathematics/equations/admittance-conductance-susceptance' },
            { label: 'Power And Effective Resistance', slug: 'mathematics/equations/power-effective-resistance' },
            { label: 'Capacity Susceptance', slug: 'mathematics/equations/capacity-susceptance' },
            { label: 'Hysteresis Law', slug: 'mathematics/equations/steinmetz-hysteresis-law' },
            { label: 'Transient Term', slug: 'mathematics/equations/transient-term' },
            { label: 'RLC Oscillation', slug: 'mathematics/equations/rlc-oscillation' },
            { label: 'Condenser Oscillation', slug: 'mathematics/equations/condenser-oscillation-decrement' },
            { label: 'Interactive Tools', slug: 'tools' }
          ]
        },
        {
          label: 'Diagrams And Glossary',
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
          label: 'Comparisons And Interpretation',
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
          label: 'Project Status',
          items: [
            { label: 'Project Tracker', slug: 'project-tracker' },
            { label: 'Publication Roadmap', slug: 'roadmap' },
            { label: 'Future Codex Architecture', slug: 'roadmap/future-codex-architecture' }
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
