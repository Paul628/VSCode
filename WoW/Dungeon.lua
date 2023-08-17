-- Mend-Frostmourne

-- Library

local LIBRARY_NAME = "Mend's Dungeon Teleport Buttons"

local Library = _G[LIBRARY_NAME]

if not Library then
    Library = CreateFrame("Frame", LIBRARY_NAME)
    
    Library.MAP_ID_TO_SPELL_IDS = {
        -- Dragonflight Season 1
        [2]   = {131204}, -- Temple of the Jade Serpent
        [165] = {159899}, -- Shadowmoon Burial Grounds
        [200] = {393764}, -- Halls of Valor
        [210] = {393766}, -- Court of Stars
        [399] = {393256}, -- Ruby Life Pools
        [400] = {393262}, -- The Nokhud Offensive
        [401] = {393279}, -- The Azure Vault
        [402] = {393273}, -- Algeth'ar Academy
        
        -- Dragonflight Season 2
        [206] = {410078}, -- Neltharion's Lair
        [245] = {410071}, -- Freehold
        [251] = {410074}, -- The Underrot
        [403] = {393222}, -- Uldaman: Legacy of Tyr
        [404] = {393276}, -- Neltharus
        [405] = {393267}, -- Brackenhide Hollow
        [406] = {393283}, -- Halls of Infusion
        [438] = {410080}, -- The Vortex Pinnacle
    }
    
    function Library:Initialize()
        if not IsAddOnLoaded("Blizzard_ChallengesUI") then
            self:RegisterEvent("ADDON_LOADED")
            return
        end
        
        WeakAuras.WatchGCD()
        
        if ChallengesFrame and type(ChallengesFrame.Update) == "function" then
            hooksecurefunc(ChallengesFrame, "Update", function () Library:CreateDungeonButtons() end)
        end
        
        Library:CreateDungeonButtons()
    end
    
    function Library:UpdateGameTooltip(parent, spellID, initialize)
        if (WeakAuras.InLoadingScreen()) then return end
        if (not initialize and not GameTooltip:IsOwned(parent)) then return end
        local Button_OnEnter = parent:GetScript("OnEnter")
        if (not Button_OnEnter) then return end
        local name = GetSpellInfo(spellID)
        
        Button_OnEnter(parent)
        
        if IsSpellKnown(spellID) then
            local start, duration = GetSpellCooldown(spellID)
            
            GameTooltip:AddLine(" ")
            GameTooltip:AddLine(name or TELEPORT_TO_DUNGEON)
            
            if not start or not duration then
                GameTooltip:AddLine(SPELL_FAILED_NOT_KNOWN, 1, 0, 0)
            elseif duration == 0 or duration == WeakAuras.gcdDuration() then
                GameTooltip:AddLine(READY, 0, 1, 0)
            else
                GameTooltip:AddLine(SecondsToTime(ceil(start + duration - GetTime())), 1, 0, 0)
            end
        else
            GameTooltip:AddLine(" ")
            GameTooltip:AddLine(name or TELEPORT_TO_DUNGEON)
            GameTooltip:AddLine(SPELL_FAILED_NOT_KNOWN, 1, 0, 0)
        end
        
        GameTooltip:Show()
        C_Timer.After(1, function () self:UpdateGameTooltip(parent, spellID) end)
    end
    
    function Library:CreateDungeonButton(parent, spellIDs)
        if (not spellIDs) then return end
        local spellID = self:SelectBestSpellID(spellIDs)
        local button = self[parent] or CreateFrame("Button", nil, parent, "InsecureActionButtonTemplate")
        button:SetAllPoints(parent)
        button:RegisterForClicks("AnyDown", "AnyUp")
        button:SetAttribute("type", "spell")
        button:SetAttribute("spell", spellID)
        button:SetScript("OnEnter", function () self:UpdateGameTooltip(parent, spellID, true) end)
        button:SetScript("OnLeave", function () if GameTooltip:IsOwned(parent) then GameTooltip:Hide() end end)
        self[parent] = button
    end
    
    function Library:CreateDungeonButtons()
        if (InCombatLockdown()) then return end
        if (not ChallengesFrame) then return end
        if (not ChallengesFrame.DungeonIcons) then return end
        
        for _, dungeonIcon in next, ChallengesFrame.DungeonIcons do
            self:CreateDungeonButton(dungeonIcon, self.MAP_ID_TO_SPELL_IDS[dungeonIcon.mapID])
        end
    end
    
    function Library:OnEvent(event, arg1)
        if event == "ADDON_LOADED" then
            if arg1 == "Blizzard_ChallengesUI" then
                self:Initialize()
                self:UnregisterEvent("ADDON_LOADED")
            end
        end
    end
    
    function Library:SelectBestSpellID(spellIDs)
        if #spellIDs > 1 then
            for _, spellID in next, spellIDs do
                if IsSpellKnown(spellID) then
                    return spellID
                end
            end
        end
        
        return spellIDs[1]
    end
    
    Library:SetScript("OnEvent", function (self, ...) self:OnEvent(...) end)
end

-- Initialize

Library:Initialize()

