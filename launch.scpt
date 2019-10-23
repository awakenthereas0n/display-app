#Runs Display App every 3 minutes

on idle
	tell application "Display"
		tell application "Display"
			run
		end tell
		return 180
	end tell
end idle