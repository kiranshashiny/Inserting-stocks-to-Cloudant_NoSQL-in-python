################################################################################
# Useful shell script to delete Database from a cURL script.
# The URL is obtained when the user creates the database.
# Replace the database name as appropriate near the end of the script.
# In this example the database is 'sdb'
#
#
#
################################################################################
curl https://7be57a6c-61cb-455a-af9c-3e3b8c392d0f-bluemix:0b3e4268a2d73219efd0432625c8130ba0e65020b6a036edccf6065a584c13cd@7be57a6c-61cb-455a-af9c-3e3b8c392d0f-bluemix.cloudant.com/sdb \
    -X DELETE \
