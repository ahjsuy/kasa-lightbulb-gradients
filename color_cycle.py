import asyncio
import time
from kasa import Discover, Module, LightState

async def updateBulb(dev, h, s, v):
    await dev.set_hsv(h, s, v)
    await dev.update()
    time.sleep(1)

async def main():
    dev = await Discover.discover_single("192.168.1.235")
    await dev.update()
    print(dev.alias)

    while True:
        # Smoother transition from cool blue to warm orange and back
        await updateBulb(dev, 210, 80, 90)  # Cool blue start
        await updateBulb(dev, 208, 78, 88)  # Slightly lighter blue
        await updateBulb(dev, 205, 76, 86)  # Lighter blue
        await updateBulb(dev, 200, 74, 84)  # Light cool blue
        await updateBulb(dev, 190, 72, 82)  # Transitioning to a cooler greenish-blue
        await updateBulb(dev, 180, 70, 80)  # Cooler shade, slight green tint
        await updateBulb(dev, 170, 68, 78)  # More greenish tint, heading to neutral
        await updateBulb(dev, 160, 66, 76)  # Greenish-cyan, neutralizing
        await updateBulb(dev, 140, 64, 74)  # Cyan, slowly warming up
        await updateBulb(dev, 120, 70, 75)  # Light cyan, hint of warmth
        await updateBulb(dev, 100, 75, 76)  # Yellow-green, subtle warmth
        await updateBulb(dev, 80, 78, 77)   # Yellowish, warm tint beginning
        await updateBulb(dev, 70, 80, 79)   # Warm yellow
        await updateBulb(dev, 60, 83, 81)   # Warmer, golden hue
        await updateBulb(dev, 50, 85, 83)   # Soft warm, rich golden hue
        await updateBulb(dev, 45, 88, 84)   # Deeper warmth
        await updateBulb(dev, 40, 90, 86)   # Warm orange beginning
        await updateBulb(dev, 35, 92, 88)   # Deepening warm orange
        await updateBulb(dev, 30, 95, 90)   # Deep warm orange

        # Smoothly transitioning back to cool blue
        await updateBulb(dev, 35, 92, 88)   # Back to warm orange
        await updateBulb(dev, 40, 90, 86)   # Lighter warm hue
        await updateBulb(dev, 45, 88, 84)   # Softer orange
        await updateBulb(dev, 50, 85, 83)   # Golden hue
        await updateBulb(dev, 60, 83, 81)   # Yellowish, transitioning to cooler
        await updateBulb(dev, 70, 80, 79)   # Yellow-green, getting cooler
        await updateBulb(dev, 80, 78, 77)   # Greenish-yellow, cooling down
        await updateBulb(dev, 100, 75, 76)  # Light cyan, moving cooler
        await updateBulb(dev, 120, 70, 75)  # Cyan, cooling further
        await updateBulb(dev, 140, 64, 74)  # Cool cyan, almost neutral
        await updateBulb(dev, 160, 66, 76)  # Greenish-cyan, cooler again
        await updateBulb(dev, 170, 68, 78)  # Slightly cooler greenish shade
        await updateBulb(dev, 180, 70, 80)  # Neutral cool shade
        await updateBulb(dev, 190, 72, 82)  # Cool blue-green tint
        await updateBulb(dev, 200, 74, 84)  # Cool blue again
        await updateBulb(dev, 205, 76, 86)  # Deepening blue
        await updateBulb(dev, 208, 78, 88)  # Near original cool blue
        await updateBulb(dev, 210, 80, 90)  # Return to original cool blue



if __name__ == "__main__":
    asyncio.run(main())

    #1584E6
    #2781D4
    #387EC2
    #457CB5
    #5379A6
    #627697
    #727386
    #837076
    #936D65
    #9E6B5A
    #AA694D
    #BA663D
    #CB632B