// created by Sean Li on Nov 6 2020
<template>
  <div class="ec-container">
    <v-stepper v-model="e1">
      <!--   Stepper Header   -->
      <v-stepper-header>
        <v-stepper-step
          :complete="e1 > 1"
          :step="step1"
          :color="step1Color"
        >
          Brand
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="e1 > 2"
          :step="step2"
          :color="step2Color"
        >
          Product category
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="e1 > 3"
          :step="step3"
          :color="step3Color"
        >
          Variation
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="e1>4"
          :step="step4"
          :color="step4Color"
        >
          Items details
        </v-stepper-step>
      </v-stepper-header>
      <!--   Stepper Content   -->
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card
            class="mb-12"
            color="rgba(0, 0, 0, 0)"
            flat
          >
            <v-form
              ref="brandInfoForm"
            >
              <v-text-field
                v-model="brandInfo.name"
                :rules="brandInfoRules.nameRules"
                label="Brand Name"
                color="accent"
                required
              >
              </v-text-field>
              <v-text-field
                v-model="brandInfo.telephone"
                :rules="brandInfoRules.telephoneRules"
                label="Phone Number"
                color="accent"
                required
              ></v-text-field>
              <v-text-field
                v-model="brandInfo.website"
                :rules="brandInfoRules.websiteRules"
                label="Brand Website"
                color="accent"
              ></v-text-field>
              <v-text-field
                v-model="brandInfo.logo"
                label="Brand Logo"
                color="accent"
              ></v-text-field>
              <v-text-field
                v-model="brandInfo.description"
                label="Brand Description"
                color="accent"
              ></v-text-field>
            </v-form>
          </v-card>
          <v-btn
            @click="brandInfoContinue"
            outlined
          >
            Continue
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card
            class="mb-12"
            color="rgba(0, 0, 0, 0)"
            flat
          >
            <v-form
              ref="productCategoryForm"
            >
              <v-select
                v-model="parentCategorySelected"
                :items="productCategory.parentCategories"
                :rules="productCategoryRules.categoriesRules"
                item-text="categoryName"
                item-value="categoryID"
                color="accent"
                label="Product Category"
                @change="changedParentCategory"
              >
              </v-select>
              <v-select
                v-model="childCategorySelected"
                :items="productCategory.childCategories"
                :rules="productCategoryRules.childCategoriesRules"
                item-text="categoryName"
                item-value="categoryID"
                color="accent"
                label="Product Sub-Category"
              >
              </v-select>
            </v-form>
          </v-card>

          <v-btn
            @click="productCategoryContinue"
            outlined
          >
            Continue
          </v-btn>

          <v-btn
            text
            @click="e1 = 1"
          >
            Back
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card
            class="mb-12"
            color="rgba(0, 0, 0, 0)"
            flat
          >
            <v-form
              ref="ProductVariationForm"
            >
              <v-text-field
                v-model="productTitle"
                :rules="productInfoRules.titleRules"
                label="Product Title"
                color="accent"
                required
              >
              </v-text-field>
              <div class="is-variation"><span>Are there variations for this product?</span></div>
              <v-radio-group
                v-model="isVariation"
              >
                <v-radio
                  label="Yes"
                  color="primary"
                  value=1
                ></v-radio>
                <v-radio
                  label="No"
                  color="primary"
                  value=0
                  @click="onNoVariation"
                ></v-radio>
              </v-radio-group>
              <div class="is-variation" v-show="isVariation==1">
                <span>Please enter the variation type (Size, Color, etc)</span>
                <v-row>
                  <v-col
                    cols="12"
                    md="3"
                    sm="6"
                  >
                    <v-text-field
                      v-model="variationKey"
                      color="accent"
                      dense
                      required
                    >
                    </v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    md="3"
                    sm="6"
                  >
                    <v-btn
                      @click="addVariation"
                      outlined
                    >
                      Add
                    </v-btn>
                  </v-col>
                </v-row>
              </div>
              <v-divider></v-divider>
              <div class="is-variation" v-show="variations.length > 0" v-for="variation in variations" :key="variation.variationKey">
                <span class="text-caption text-md-h6">Variation:
                  <v-chip
                    close
                    outlined
                    ma-1
                    @click:close="deleteVariationValueClicked(variation.variationKey)"
                  >
                    {{variation.variationKey}}
                  </v-chip>
                </span><br />
                <span>Please enter the variation value below:</span><br />
                <v-chip
                  v-for="value in variation.variationValue" :key="value"
                  close
                  outlined
                  ma-1
                  @click:close="deleteVariationClicked(variation.variationKey, value)"
                >
                  {{value}}
                </v-chip>
                <v-row>
                  <v-col
                    cols="12"
                    md="3"
                    sm="6"
                  >
                    <v-text-field
                      :id="variation.variationKey"
                      color="accent"
                      required
                      cols="12"
                      md="4"
                    >
                    </v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    md="3"
                    sm="6"
                  >
                    <v-btn
                      @click="addVariationValue(variation.variationKey)"
                      outlined
                    >
                      Add
                    </v-btn>
                  </v-col>
                </v-row>
              </div>
            </v-form>
          </v-card>

          <v-btn
            @click="variationContinue"
            outlined
          >
            Continue
          </v-btn>

          <v-btn
            text
            @click="e1 = 2"
          >
            Back
          </v-btn>
        </v-stepper-content>

        <v-stepper-content color="accent" step="4">
          <v-card
            class="mb-12"
            color="rgba(0, 0, 0, 0)"
            flat
          >
            <v-form
              ref="itemsDetailsForm"
            >
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Title"
                color="accent"
                required
              >
              </v-text-field>
              <v-currency-field
                :rules="productInfoRules.titleRules"
                label="Item Price"
                color="accent"
                prefix="$"
                required
              >
              </v-currency-field>
              <v-currency-field
                :rules="productInfoRules.titleRules"
                label="Item Sell Price"
                color="accent"
                prefix="$"
                required
              >
              </v-currency-field>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Stock"
                color="accent"
                required
              >
              </v-text-field>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Weight"
                color="accent"
                suffix="lbs"
              >
              </v-text-field>
              <div>Item Dimension</div>
              <v-row>
                <v-col
                  cols="4"
                  md="4"
                  sm="4"
                >
                  <v-text-field
                    :rules="productInfoRules.titleRules"
                    label="Item Width"
                    color="accent"
                    suffix="inch"
                  >
                  </v-text-field>
                </v-col>
                <v-col
                  cols="4"
                  md="4"
                  sm="4"
                >
                  <v-text-field
                    :rules="productInfoRules.titleRules"
                    label="Item Length"
                    color="accent"
                    suffix="inch"
                  >
                  </v-text-field>
                </v-col>
                <v-col
                  cols="4"
                  md="4"
                  sm="4"
                >
                  <v-text-field
                    :rules="productInfoRules.titleRules"
                    label="Item Height"
                    color="accent"
                    suffix="inch"
                  >
                  </v-text-field>
                </v-col>
              </v-row>
              <div>Item Features</div>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Feature 1"
                color="accent"
              >
              </v-text-field>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Feature 2"
                color="accent"
              >
              </v-text-field>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Feature 3"
                color="accent"
              >
              </v-text-field>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Feature 4"
                color="accent"
              >
              </v-text-field>
              <v-text-field
                :rules="productInfoRules.titleRules"
                label="Item Feature 5"
                color="accent"
              >
              </v-text-field>
            </v-form>
          </v-card>

          <v-btn
            @click="itemsDetailsContinue"
            outlined
          >
            Continue
          </v-btn>

          <v-btn
            text
            @click="e1 = 3"
          >
            Back
          </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>
<script>
export default {
  name: "NewProduct",
  components: {
  },
  data: () => ({
    e1: 1,

    // Step 1 is for brand info
    step1: 1,
    step1Color: "primary",
    brandInfo: {
      name: "",
      telephone: "",
      website: "",
      logo: "",
      description: "",
    },
    brandInfoRules: {
      nameRules: [
        v => !!v || "Name is required"
      ],
      telephoneRules: [
        v => !!v || "Telephone is required",
        v => /^(\(?\+?[0-9]*\)?)?[0-9]*$/.test(v) || "Only numbers are allowed.",
        v => v.length >= 10 || "At least 10 digits."
      ],
      websiteRules: [
        v => !v || /[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&//=]*)/.test(v) || "Please enter a valid website address."
      ],
    },

    // Step 2 is for product category and sub-category.
    step2: 2,
    step2Color: "primary",
    productCategory: {
      parentCategories: [{
        categoryName: "",
        categoryID: null
      }],
      childCategories: [{
        categoryName: "",
        categoryID: null
      }]
    },
    productCategoryRules: {
      categoriesRules: [
        v => !!v || "Please select a product category."
      ],
      childCategoriesRules: [
        v => !!v || v===0 || "Please select a product sub-category."
      ],
    },
    parentCategorySelected: null,
    childCategorySelected: null,

    // Step 3 is for product title and variation.
    step3: 3,
    step3Color: "primary",
    productTitle:"",
    productInfoRules: {
      titleRules:  [
        v => !!v || "Product title is required",
      ],
    },
    isVariation: null,
    variationKey: "",
    variations: [],

    //step 4 is for items details
    step4: 4,
    step4Color: "primary",
    itemsDetails: [],
    testPrice: 10,
    itemsDetailsRules: {
      titleRules:  [
        v => !!v || "Product title is required",
      ],
      priceRules: [
        v => !!v || "Item price is required",
        v => v.length <= 50 || "Max 50 characters",

      ]
    }

  }),
  mounted(){
      this.$http.getCategories().then(response => {
        let dataItems = response.data
        const categoriesList = []
        for (let categories of dataItems){
          categoriesList.push({
            categoryName: categories.name,
            categoryID: categories.id
          })
        }
        this.productCategory.parentCategories = categoriesList
      })
  },
  methods: {
    brandInfoContinue(){
      if(!this.$refs.brandInfoForm.validate()){
        this.$message.error("Please fix the invalid input to continue.")
        this.step1 = "!"
        this.step1Color = "error"
      }else{
        this.e1 = 2
        this.step1Color = "primary"
      }
    },
    changedParentCategory(){
      // When ParentCategory changed, reset childCategory selected to null.
      // Clients need to re-select.
      this.childCategorySelected = null
      // And then get childCategories again from server side.
      this.$http.getCategories(this.parentCategorySelected).then(response => {
        let childDataItems = response.data
        if(childDataItems.length > 0){
          const childCategoriesList = []
          for (let childCategories of childDataItems){
            childCategoriesList.push({
              categoryName: childCategories.name,
              categoryID: childCategories.id
            })
          }
          this.productCategory.childCategories = childCategoriesList
        }else{
          this.productCategory.childCategories = [{
            categoryName: "Not sub category are available.",
            categoryID: 0
          },]
        }
      }).catch(error => {
        this.$message.error(error.response)
      })
    },
    productCategoryContinue(){
      if(!this.$refs.productCategoryForm.validate()){
        this.$message.error("Please fix the invalid input to continue.")
        this.step2 = "!"
        this.step2Color = "error"
      }else{
        this.e1 = 3
        this.step2Color = "primary"
      }
    },
    onNoVariation(){
      this.variations = []
    },
    addVariation(){
      // check if a variation key is entered for the input
      if(this.variationKey){
        let variationObj = {
          variationKey: this.variationKey.toLowerCase(),
          variationValue: []
        }
        // check if variation key has been added or not
        if(this.variations.length !== 0){
          let newVariationKey = variationObj.variationKey.toLowerCase()
          let existVariationKeyAry = []
          for (let variation of this.variations){
            let existVariationKey = variation.variationKey.toLowerCase()
            existVariationKeyAry.push(existVariationKey)
          }
          let is_exist = existVariationKeyAry.indexOf(newVariationKey)
          // check if new variation key exists or not
          if(is_exist >= 0){
            this.$message.error("The variation '" + newVariationKey + "' already exists.")
          }else{
            this.variations.push(variationObj)
            this.variationKey = null
          }
        }else{
          this.variations.push(variationObj)
          this.variationKey = null
        }
      }else{
        this.$message.error("Please enter a variation.")
      }
    },
    deleteVariationValueClicked(variationKey){
      let targetVariationKey = variationKey
      for(let i=0; i<this.variations.length; i++){
        let existVariationKey = this.variations[i].variationKey
        if(existVariationKey == targetVariationKey){
          this.variations.splice(i, 1)
        }
      }
    },
    addVariationValue(variationKey){
      // get the variation key param for the btn clicked
      let targetVariationKey = variationKey.toLowerCase()

      // if new value is entered in the input
      if(document.getElementById(variationKey).value){
        let newVariationValue = document.getElementById(variationKey).value.toLowerCase()

        //loop each variation data item
        for (let variation of this.variations){
          let variationKey = variation.variationKey.toLowerCase()
          let existVariationValueAry = variation.variationValue

          // check if the variation key matches
          if(targetVariationKey == variationKey){
            // check if the new value not exists,then push the value to this variation key
            let index = existVariationValueAry.indexOf(newVariationValue)
            if(index < 0){
              variation.variationValue.push(document.getElementById(variationKey).value);
              document.getElementById(variationKey).value = ""
            }else{
              this.$message.error("The value '" + newVariationValue + "' already exists.")
            }
          }
        }
        document.getElementById(variationKey).value = ""
      }else{
        this.$message.error("Please enter a value for the variation " + "'" + targetVariationKey + "'")
      }
    },
    deleteVariationClicked(key, value){
      let targetVariationKey = key
      let targetVariationValue = value
      for (let variation of this.variations){
        let variationKey = variation.variationKey
        if(targetVariationKey == variationKey){
          let index = variation.variationValue.indexOf(targetVariationValue);
          if(index !== -1){
            variation.variationValue.splice(index, 1);
          }
        }
      }
    },
    variationContinue(){
      let variationValid = false
      if(this.$refs.ProductVariationForm.validate()){
        if(this.isVariation==0){
          variationValid = true
        }else{
          if(this.variations.length > 0){
            for(let i=0; i<this.variations.length; i++){
              if(this.variations[i].variationValue.length > 0){
                variationValid = true
              }
            }
          }
        }
      }
      if(variationValid){
        this.e1 = 4
        this.step3Color = "primary"
      }else{
        this.$message.error("Please fix the invalid input to continue.")
        this.step3 = "!"
        this.step3Color = "error"
      }
    },
    itemsDetailsContinue(){
      this.e1 = 5
      this.step4Color = "primary"
    },
  }
};
</script>
<style scoped lang="scss">

</style>