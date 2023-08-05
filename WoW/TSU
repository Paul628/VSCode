function(s, e, msg, ...)
    
    if msg == nil then
        return false
    end
    if e=="OPTIONS" then
    end
    
    
    
    if e=="CHAT_MSG_SAY" or e=="CHAT_MSG_PARTY" or e=="CHAT_MSG_PARTY_LEADER" or e=="CHAT_MSG_RAID" or e=="CHAT_MSG_RAID_LEADER" then
        
        
        itemColor, itemString, itemName, roll = msg:match("|c(.*)|H(.*)|h%[(.*)%]|h|r%s*%a*%s*(%d*)")
        
        if not itemColor then
            return false
        else
            _, itemLink = GetItemInfo(itemString)
            if not itemLink then 
                return false
            end
        end
        itemID=select(2,strsplit(":",itemString,3))
        itemIcon = GetItemIcon(itemID)
        sourceName= select(1,...)
        roll=tonumber(roll)
        sourceName=strsplit("-",sourceName)
        ident=sourceName..itemLink
        identroll=itemLink..roll
        --print(ident)
        
        aura_env.identI=ident
        s[ident] = {
            show = true,
            changed = true,
            progressType = "timed",
            duration = aura_env.config["duration"],
            expirationTime = GetTime()+aura_env.config["duration"],
            icon = itemIcon,
            autoHide = true,
            link=itemLink,
            playerName=sourceName,
            maxroll=roll,
            roll=0,
            highroller=""
            
        }
        
        
        return true
        
        
        
    elseif e=="PLAYER_ROLLED_ON" or e=="CHAT_MSG_SYSTEM" then
        
        local boolean=msg:find("%a*%s%a*%s%d*%s%(%d?-%d*%)")
        if boolean==nil then
            return false
        end
        
        local player,roll,rollon=msg:match("(%a*)%s%a*%s(%d*)%s%(%d?-(%d*)%)")
        
        --player=msg
        --roll, rollon=...
        roll=tonumber(roll)
        rollon=tonumber(rollon)
        for _,v in pairs(s) do
            v.expirationTime = GetTime()+aura_env.config["duration"]
            
            if v.maxroll==rollon then
                
                if roll>v.roll then
                    v.roll=roll
                    v.highroller=player
                    
                    
                end
                
                v.changed = true
                return true    
                
            end
            
        end    
        
    end
    
    
end


