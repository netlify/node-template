import { expect, test } from 'vitest'

import { mainFunction } from './main.js'

test('Template test', () => {
  expect(mainFunction()).toBe(true)
})
