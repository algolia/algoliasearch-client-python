package com.algolia.codegen.utils;

import com.algolia.codegen.Utils;
import java.util.*;
import org.openapitools.codegen.CodegenModel;
import org.openapitools.codegen.CodegenProperty;
import org.openapitools.codegen.model.ModelsMap;

public class OneOfUtils {

  private OneOfUtils() {
    // Empty.
  }

  public static void updateModelsOneOf(Map<String, ModelsMap> models, String modelPackage) {
    for (ModelsMap modelContainer : models.values()) {
      // modelContainers always have 1 and only 1 model in our specs
      var model = modelContainer.getModels().get(0).getModel();
      if (model.oneOf.isEmpty()) continue;
      markOneOfChildren(models, model);
      generateSealedChildren(models, modelPackage, model);
      model.vendorExtensions.put("x-is-one-of", true);
      model.vendorExtensions.put("x-one-of-explicit-name", Utils.shouldUseExplicitOneOfName(model.oneOf));
    }
  }

  private static void generateSealedChildren(Map<String, ModelsMap> models, String modelPackage, CodegenModel model) {
    var sealedChilds = new ArrayList<>();
    for (String oneOf : model.oneOf) {
      ModelsMap modelsMap = models.get(oneOf);
      if (modelsMap != null) {
        CodegenModel compoundModel = modelsMap.getModels().get(0).getModel();
        compoundModel.vendorExtensions.put("x-one-of-explicit-name", compoundModel.classname);
        compoundModel.vendorExtensions.put("x-fully-qualified-classname", modelPackage + "." + compoundModel.classname);
        compoundModel.vendorExtensions.put("x-classname-or-alias", compoundModel.classname + "Impl");
        sealedChilds.add(compoundModel);
      } else {
        CodegenModel newModel = new CodegenModel();
        String name = oneOf.replace("<", "Of").replace(">", "");
        newModel.setClassname(name + "Wrapper");
        newModel.setDescription(model.classname + " as " + oneOf);
        CodegenProperty property = new CodegenProperty();
        property.setName("value");
        property.setRequired(true);
        property.setDatatypeWithEnum(oneOf);
        newModel.setVars(Collections.singletonList(property));
        newModel.vendorExtensions.put("x-is-number", newModel.isNumber);
        newModel.vendorExtensions.put("x-one-of-explicit-name", isNumberType(oneOf) ? "Number" : name);
        newModel.vendorExtensions.put("x-fully-qualified-classname", newModel.classname);
        sealedChilds.add(newModel);
      }
    }
    model.vendorExtensions.put("x-sealed-childs", sealedChilds);
  }

  private static void markOneOfChildren(Map<String, ModelsMap> models, CodegenModel model) {
    var oneOfList = new ArrayList<Map<String, Object>>();
    for (String oneOf : model.oneOf) {
      var oneOfModel = new HashMap<String, Object>();
      oneOfModel.put("type", oneOf);
      oneOfModel.put("name", oneOf.replace("<", "Of").replace(">", ""));
      oneOfModel.put("listElementType", oneOf.replace("List<", "").replace(">", ""));
      oneOfModel.put("isList", oneOf.contains("List"));
      markCompounds(models, oneOf, oneOfModel, model);
      oneOfList.add(oneOfModel);
    }
    oneOfList.sort(comparator); // have fields with "discriminators" in the start of the list
    model.vendorExtensions.put("x-one-of-list", oneOfList);
  }

  private static void markCompounds(Map<String, ModelsMap> models, String oneOf, Map<String, Object> oneOfModel, CodegenModel model) {
    // 1. Find child model
    var modelsMap = models.get(oneOf);
    if (modelsMap == null) return;
    oneOfModel.put("isObject", true);

    // 2. add the child to parent model
    var compoundModel = modelsMap.getModels().get(0).getModel();
    oneOfModel.put("child", compoundModel.classname);

    // 3. mark the child and add its parent (may have many)
    compoundModel.vendorExtensions.put("x-one-of-element", true);
    var parentInfo = new HashMap<String, String>();
    parentInfo.put("parent_classname", model.classname);
    compoundParent(compoundModel).add(parentInfo);
    //noinspection unchecked
    var values = (List<String>) compoundModel.vendorExtensions.get("x-discriminator-fields");
    if (values != null) {
      List<Map<String, String>> newValues = values.stream().map(value -> Collections.singletonMap("field", value)).toList();
      oneOfModel.put("discriminators", newValues);
    }
  }

  private static Set<Map<String, String>> compoundParent(CodegenModel model) {
    //noinspection unchecked
    var parents = (Set<Map<String, String>>) model.vendorExtensions.get("x-one-of-element-parents");
    if (parents != null) return parents;
    parents = new HashSet<>();
    model.vendorExtensions.put("x-one-of-element-parents", parents);
    return parents;
  }

  private static boolean isNumberType(String typeName) {
    return typeName.equals("Int") || typeName.equals("Double") || typeName.equals("Long");
  }

  private static final Comparator<Map<String, Object>> comparator = (mapA, mapB) -> {
    boolean hasDiscriminatorA = mapA.containsKey("discriminators");
    boolean hasDiscriminatorB = mapB.containsKey("discriminators");
    // Maps with "discriminators" come first
    if (hasDiscriminatorA && !hasDiscriminatorB) {
      return -1;
    } else if (!hasDiscriminatorA && hasDiscriminatorB) {
      return 1;
    } else {
      // If both maps have or don't have "discriminators," compare their list lengths
      if (hasDiscriminatorA && hasDiscriminatorB) {
        List<?> discriminatorsA = (List<?>) mapA.get("discriminators");
        List<?> discriminatorsB = (List<?>) mapB.get("discriminators");

        // Compare the lengths of the lists
        return discriminatorsB.size() - discriminatorsA.size();
      }

      // If the lengths are the same or both maps don't have "discriminators," return 0
      return 0;
    }
  };
}
