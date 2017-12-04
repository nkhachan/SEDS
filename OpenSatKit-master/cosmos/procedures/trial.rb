i = 0
while i < 200
  value = tlm("VULCAN2 SOH DISTANCE")
  puts value
  cmd("PRESSTABLE INTENSITY with PIN_STATUS #{value}")
  i += 1
end


