package creational.abstractFactory

import creational.abstractFactory.forges.RitoForge

fun main() {
    val forgeMenu = ForgeMenu(RitoForge())
    forgeMenu.displayEquipments()
}