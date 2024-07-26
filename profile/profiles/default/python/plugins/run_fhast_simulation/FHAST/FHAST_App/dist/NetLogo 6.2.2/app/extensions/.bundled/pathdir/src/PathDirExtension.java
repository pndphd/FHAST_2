// PathDirExtension - V 3.1.0 (May 2019)
// Charles Staelin, Smith College

/*
 * Contains a number of procedures for finding paths, for creating,
 * renaming and deleting directories, and for finding file sizes and dates.
 * REMEMBER THAT ANY PROCEDURES THAT FOOL WITH YOUR FILES MAY BE DANGEROUS!
 */

/* Written for NetLogo v6.1 and for Java 1.8.
 */

package org.nlogo.extensions.pathdir;

import org.nlogo.api.*;
import org.nlogo.core.Syntax;
import org.nlogo.core.SyntaxJ;

import java.io.File;
import java.util.Date;
import java.text.SimpleDateFormat;
import java.io.IOException;

public class PathDirExtension extends org.nlogo.api.DefaultClassManager {
  
  private static org.nlogo.workspace.ExtensionManager em;
  
  @Override
  // runOnce is no longer used, but left here in case it might be useful
  // in the future. It gets and holds the current ExtensionManager.
  public void runOnce(org.nlogo.api.ExtensionManager em) 
          throws org.nlogo.api.ExtensionException {
    PathDirExtension.em = (org.nlogo.workspace.ExtensionManager) em;
  }

  // Prepends to the attachName argument the current working directory as
  // specified in the NetLogo model's context.  However, if attachName is an
  // absolute path, it is returned unchanged.
  private static String attachCWD(Context context, String attachName) 
          throws ExtensionException {
    if (attachName.length() == 0) {
      attachName = ".";
    }
    try {
      attachName = context.attachCurrentDirectory(attachName);
    } catch (java.net.MalformedURLException ex) {
      throw new ExtensionException(ex);
    }

    File f = new File(attachName);
    try {
      return (f.getCanonicalFile()).toString();
    } catch (IOException ex) {
      ExtensionException eex = new ExtensionException(ex);
      eex.setStackTrace(ex.getStackTrace());
      throw eex;
    }
  }
  
  // strips the path and the file extension from the string.
  // should be pretty robust with wierd paths and filenames.
  private static String getFilenameOnly(String s) {

    String separator = File.separator;
    String filename;

    // Remove the path upto the filename.
    int lastSeparatorIndex = s.lastIndexOf(separator);
    if (lastSeparatorIndex == -1) {
        filename = s;
    } else {
        filename = s.substring(lastSeparatorIndex + 1);
    }

    // Remove the extension.
    int extensionIndex = filename.lastIndexOf(".");
    if (extensionIndex == -1)
        return filename;

    return filename.substring(0, extensionIndex);
}

  @Override
  public void load(org.nlogo.api.PrimitiveManager primManager) {
    primManager.addPrimitive("get-separator", new getSeparator());
    primManager.addPrimitive("get-model-path", new getModelDirectory());
    primManager.addPrimitive("get-home-path", new getHomeDirectory());
    primManager.addPrimitive("get-CWD-path", new getCurrentDirectory());
    primManager.addPrimitive("get-model-name", new getModelName());
    primManager.addPrimitive("get-model-file", new getModelFile());
    primManager.addPrimitive("create", new createDirectory());
    primManager.addPrimitive("isDirectory?", new isDirectory());
    primManager.addPrimitive("list", new listDirectory());
    primManager.addPrimitive("move", new moveFileOrDirectory());
    primManager.addPrimitive("delete", new deleteDirectory());
    primManager.addPrimitive("exists?", new fileExists());
    primManager.addPrimitive("get-size", new getFileSize());
    primManager.addPrimitive("get-date-ms", new getFileDateTimeInMS());
    primManager.addPrimitive("get-date", new getFileDateTimeAsString());
  }

  // Returns the path separator for the current operating system, for 
  // use in creating new path strings in NetLogo.
  public static class getSeparator implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException {
      return File.separator;
    }
  }

  // Returns the absolute directory path to the users home directory,
  // as specified "user.home" environment variable in the current
  // operating system.
  public static class getHomeDirectory implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException {

      String homeDirName = System.getProperty("user.home");
      File f = new File(homeDirName);
      try {
        return (f.getCanonicalFile()).toString();
      } catch (IOException ex) {
        ExtensionException eex = new ExtensionException(ex);
        eex.setStackTrace(ex.getStackTrace());
        throw eex;
      }
    }
  }

  // Returns the absolute directory path to the current working directory
  // as specified in the NetLogo model's context.
  public static class getCurrentDirectory implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException {
      return attachCWD(context, ".");
    }
  }

  // Returns the name of the NetLogo model. This will always be the name of 
  // the .nlogo or .nlogo3d file that contains the model, without the file
  // extension. If the current model has not been yet saved to a file, NetLogo 
  // displays it "Untitled", but we return an empty string.
  // In v6.0, the workspace is directly available from the context and the 
  // model's filename (if it has yet been set) from that. In prior versions
  // we used the display name, but it turns out that the display name is not
  // set in BehaviorSpace runs other than the ones actually displayed, and 
  // thus it comes back as "Untitled". So we go with stripping the extension
  // from the filename.
  public static class getModelName implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException {

      Workspace wkspc = context.workspace();
//      String modelName = ((AbstractWorkspace) wkspc).modelNameForDisplay();
      String modelName = getFilenameOnly(wkspc.getModelFileName());
      if ( modelName.equals("Untitled") ) {
        modelName = "";
      }
      
      return modelName;
    }
  }
  
  // Returns the name of the .nlogo or .nlogo3d file that contains the 
  // current model.  If the current model has not yet been saved to a file, 
  // returns an empty string.
  public static class getModelFile implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException {

      Workspace wkspc = context.workspace();
      String modelFile = wkspc.getModelFileName();
      if (modelFile == null) {
        modelFile = "";
      }
      
      return modelFile;
    }
  }
  
  // Returns the absolute path to the directory containing the current model.
  // If the current model has not yet been saved to a file, returns an empty
  // string.
  public static class getModelDirectory implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException {

      Workspace wkspc = context.workspace();
      String modelDir = wkspc.getModelDir();
      if (modelDir == null) {
        modelDir = "";
      }

      return modelDir;
    }
  }

  // Creates a directory.  If the input string does not contain an 
  // absolute path, the directory is created relative to the current 
  // working directory specified in the NetLogo model's context.
  // Note that this procedure will create as many intermediate directories
  // as are needed to create the final directory in the specified path.
  // If the directory already exists, nothing is done.
  public static class createDirectory implements Command {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.commandSyntax(new int[]{Syntax.StringType()});
    }

    @Override
    public void perform(Argument args[], Context context) throws ExtensionException, LogoException {

      File f = new File(attachCWD(context, args[0].getString()));
      if (!f.exists()) {
        boolean success = f.mkdirs();
        if (!success) {
          throw new ExtensionException("Could not create the directory at " + f.toString() + ".");
        }
      }
    }
  }

  // Returns TRUE if the argument both exists and is a directory; otherwise, 
  // returns FALSE.
  public static class isDirectory implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(new int[]{Syntax.StringType()}, Syntax.BooleanType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException, LogoException {

      File f = new File(attachCWD(context, args[0].getString()));
      return f.exists() && f.isDirectory();
    }
  }

  // Returns a NetLogo list of strings, with each string being an element
  // of the listing of the specified directory.  If the input string does
  // not contain an absolute path, the path is assumed to be relative to 
  // the current working directory as specified in the NetLogo model's
  // context.
  public static class listDirectory implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(new int[]{Syntax.StringType()}, Syntax.ListType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException, LogoException {

      File f = new File(attachCWD(context, args[0].getString()));
      if (!f.exists() || !f.isDirectory()) {
        throw new ExtensionException(f.toString() + " does not exist as a directory.");
      }

      String[] dirListArray = f.list();
      LogoListBuilder dirList = new LogoListBuilder();
      for (String dirListArray1 : dirListArray) {
        dirList.add(dirListArray1);
      }
      return dirList.toLogoList();
    }
  }

  // moves the file or directory in the first input string to the new
  // name and/or location in the second input string.  It can simply be used
  // to rename a file or directory as well.  If either input string does not
  // contain an absolute path, it assumes the directory or file is located in
  // the current working directory as specified in the NetLogo model's context.
  public static class moveFileOrDirectory implements Command {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.commandSyntax(new int[]{Syntax.StringType(),
        Syntax.StringType()});
    }

    @Override
    public void perform(Argument args[], Context context) throws ExtensionException, LogoException {

      File fOldName = new File(attachCWD(context, args[0].getString()));
      if (!(fOldName.exists())) {
        throw new ExtensionException("Source file or directory " + fOldName.toString()
                + " does not exist.");
      }

      File fNewName = new File(attachCWD(context, args[1].getString()));
      if (fNewName.exists()) {
        throw new ExtensionException("The destination " + fNewName.toString()
                + " already exists.");
      }

      boolean flag = fOldName.renameTo(fNewName);
      if (!flag) {
        throw new ExtensionException("Could not rename/move " + fOldName.toString()
                + " to " + fNewName.toString() + ".");
      }
    }
  }

  // deletes a directory.  If the input string does not contain an
  // absolute path, it assumes the directory to be deleted is in the
  // current working directory as specified by the NetLogo model's context.
  // Only directories may be deleted (as there is already a NetLogo
  // primitive for files) and the directory must be
  // both empty and not hidden.
  public static class deleteDirectory implements Command {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.commandSyntax(new int[]{Syntax.StringType()});
    }

    @Override
    public void perform(Argument args[], Context context) throws ExtensionException, LogoException {

      File f = new File(attachCWD(context, args[0].getString()));
      if (!f.exists() || !f.isDirectory()) {
        throw new ExtensionException(f.toString() + " does not exist as a directory.");
      }
      if (f.isHidden()) {
        throw new ExtensionException(f.toString() + " is hidden and will not be deleted.");
      }
      if (f.list().length != 0) {
        throw new ExtensionException(f.toString() + " is not empty and will not be deleted.");
      }

      boolean flag = f.delete();
      if (!flag) {
        throw new ExtensionException(f.toString() + " could not be deleted.");
      }
    }
  }

  // Returns true if the file exists; otherwise false.
  public static class fileExists implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(new int[]{Syntax.StringType()}, Syntax.BooleanType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException, LogoException {

      File fName = new File(attachCWD(context, args[0].getString()));
      return fName.exists();
    }
  }

  // Returns the size of the file in bytes.
  public static class getFileSize implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(new int[]{Syntax.StringType()}, Syntax.NumberType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException, LogoException {

      File fName = new File(attachCWD(context, args[0].getString()));
      if (!(fName.exists())) {
        throw new ExtensionException("Source file or directory " + fName.toString()
                + " does not exist.");
      }

      return (double) fName.length();
    }
  }

  // Returns the modify date of the file in milliseconds since the start of 
  // system time.
  public static class getFileDateTimeInMS implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(new int[]{Syntax.StringType()}, Syntax.NumberType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException, LogoException {

      File fName = new File(attachCWD(context, args[0].getString()));
      if (!(fName.exists())) {
        throw new ExtensionException("Source file or directory " + fName.toString()
                + " does not exist.");
      }

      return (double) fName.lastModified();
    }
  }

  // Returns the modify date/time of the file as a string.
  public static class getFileDateTimeAsString implements Reporter {

    @Override
    public Syntax getSyntax() {
      return SyntaxJ.reporterSyntax(new int[]{Syntax.StringType()}, Syntax.StringType());
    }

    @Override
    public Object report(Argument args[], Context context) throws ExtensionException, LogoException {

      File fName = new File(attachCWD(context, args[0].getString()));
      if (!(fName.exists())) {
        throw new ExtensionException("Source file or directory " + fName.toString()
                + " does not exist.");
      }

      return new SimpleDateFormat("dd-MM-yyyy HH-mm-ss").format(new Date(fName.lastModified()));
    }
  }
}
